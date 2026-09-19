#!/usr/bin/env python3
"""skill-image: 架构图 + 场景插图生成器
用法:
  python3 gen.py --arch "prompt" [name]     # 架构图 1792x1024 ¥0.5/张
  python3 gen.py --scene "prompt" [name]    # 场景图 1024x1024 ¥0.3/张
  python3 gen.py --batch-arch <json_file>   # 批量架构图

凭据: 自动读取 FMODE_API_KEY (env/config)
"""
import json, base64, urllib.request, os, sys

API = 'https://api.fmode.cn/v1/images/generations'

def _get_key():
    for src_name, src_val in [
        ('FMODE_API_KEY env', os.environ.get('FMODE_API_KEY', '')),
        ('ANTHROPIC_AUTH_TOKEN env', os.environ.get('ANTHROPIC_AUTH_TOKEN', '')),
    ]:
        if src_val and '***' not in src_val and len(src_val) > 10:
            return src_val
    try:
        with open(os.path.expanduser('~/.fmode/config.json')) as f:
            c = json.load(f)
            for k in ('api_key', 'FMODE_API_KEY'):
                if c.get(k): return c[k]
    except: pass
    try:
        with open(os.path.expanduser('~/.fmode/config.yaml')) as f:
            for l in f:
                for kw in ('api_key', 'FMODE_API_KEY'):
                    if kw in l:
                        v = l.split(':')[1].strip().strip('"\'')
                        if v and v != '${FMODE_API_KEY}': return v
    except: pass
    for p in ['/opt/data/.env', '.env']:
        try:
            with open(p) as f:
                for l in f:
                    if 'FMODE_API_KEY' in l:
                        v = l.split('=')[1].strip().strip('"\'')
                        if v and '***' not in v and len(v) > 10: return v
        except: pass
    print('❌ 未找到 API Key。设置环境变量 FMODE_API_KEY 或 ~/.fmode/config.json')
    sys.exit(1)

API_KEY = _get_key()

def _call_api(prompt, size):
    body = json.dumps({"model": "gpt-image-2.5-sunburst", "prompt": prompt, "n": 1, "size": size}).encode()
    req = urllib.request.Request(API, data=body,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method='POST')
    resp = urllib.request.urlopen(req, timeout=300)
    data = json.loads(resp.read())
    if 'b64_json' in data['data'][0]:
        return base64.b64decode(data['data'][0]['b64_json'])
    if 'url' in data['data'][0]:
        return urllib.request.urlopen(data['data'][0]['url'], timeout=60).read()
    raise Exception('No image data')

def gen_arch(prompt, name='arch'):
    """架构图: 1792x1024 ¥0.5/张，纯白底PPT用"""
    full = f'纯白背景扁平风格架构图。{prompt} 简洁扁平商务风格，纯白背景适合PPT。'
    out = _gen(full, '1792x1024', name)
    return out

def gen_scene(prompt, name='scene'):
    """场景/插图: 1024x1024 ¥0.3/张，照片/示意图/画面"""
    full = f'扁平插画场景。{prompt} 清新明亮风格。'
    out = _gen(full, '1024x1024', name)
    return out

def _gen(prompt, size, name):
    outdir = os.environ.get('SKILL_IMAGE_OUTPUT', '.')
    os.makedirs(outdir, exist_ok=True)
    path = f'{outdir}/{name}.png'
    data = _call_api(prompt, size)
    with open(path, 'wb') as f:
        f.write(data)
    sz = os.path.getsize(path)//1024
    print(f'✅ {sz}KB -> {path}')
    return path

def batch_arch(items):
    """items: [(name, prompt), ...]"""
    for name, prompt in items:
        print(f'{name}:', end=' ', flush=True)
        try:
            gen_arch(prompt, name)
        except Exception as e:
            print(f'❌ {e}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    mode, content = sys.argv[1], sys.argv[2]
    name = sys.argv[3] if len(sys.argv) > 3 else 'output'
    {'--arch': lambda: gen_arch(content, name),
     '--scene': lambda: gen_scene(content, name)}.get(mode, lambda: print(f'Unknown mode {mode}'))()