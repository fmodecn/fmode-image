#!/usr/bin/env python3
"""
fmode-image v2.0 — 架构图/应用界面/场景插图/整页PPT生成器

用法:
  python3 gen.py --arch    "prompt" [name]    架构图 1792x1024 ¥0.5
  python3 gen.py --app     "prompt" [name]    应用界面 1792x1024 ¥0.5
  python3 gen.py --explode "prompt" [name]    爆炸图 1792x1024 ¥0.5
  python3 gen.py --scene   "prompt" [name]    场景插图 1024x1024 ¥0.3
  python3 gen.py --detail  "prompt" [name]    细节图 1024x1024 ¥0.3
  python3 gen.py --slide   "prompt" [name]    整页PPT 1920x1080 ¥0.5

凭据: 自动读取 FMODE_API_KEY (env/config.json/.env)
输出: 白底PNG，SKILL_IMAGE_OUTPUT 控制输出目录
"""
import json, base64, urllib.request, os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

API = 'https://api.fmode.cn/v1/images/generations'

MODES = {
    '--arch':    {'prefix':'纯白背景扁平风格架构图。','suffix':'简洁扁平商务风格，纯白背景适合PPT。','size':'1792x1024','cost':0.5,'desc':'架构/分层/闭环图'},
    '--app':     {'prefix':'现代SaaS应用界面截图，浅色主题。','suffix':'界面细节清晰锐利，中文界面文字，像真实在运行的产品。','size':'1792x1024','cost':0.5,'desc':'产品界面(表现力最强)'},
    '--explode': {'prefix':'技术爆炸图，内部分层剖开并标注数据流向。','suffix':'扁平科技风格，纯白背景，层级与流向清晰。','size':'1792x1024','cost':0.5,'desc':'内部运转/拆解图'},
    '--scene':   {'prefix':'扁平插画场景。','suffix':'清新明亮风格。','size':'1024x1024','cost':0.3,'desc':'场景/人物/痛点插图'},
    '--detail':  {'prefix':'精密细节特写图。','suffix':'写实质感，清晰锐利。','size':'1024x1024','cost':0.3,'desc':'零件/材质/实物特写'},
    '--slide':   {'prefix':'一页16:9演示幻灯片。','suffix':'留白充足，字号层级分明，商务演示风格。','size':'1920x1080','cost':0.5,'desc':'整页PPT直接使用'},
}

def _get_key():
    for v in [os.environ.get('FMODE_API_KEY',''), os.environ.get('ANTHROPIC_AUTH_TOKEN','')]:
        if v and '***' not in v and len(v) > 10: return v
    try:
        with open(os.path.expanduser('~/.fmode/config.json'),encoding='utf-8') as f:
            c = json.load(f)
            for k in ('api_key','FMODE_API_KEY','fmodeApiToken'):
                if c.get(k): return c[k]
    except: pass
    try:
        with open(os.path.expanduser('~/.fmode/config.yaml'),encoding='utf-8') as f:
            for l in f:
                for kw in ('api_key','FMODE_API_KEY','fmodeApiToken'):
                    if kw in l:
                        v = l.split(':',1)[1].strip().strip('"\'')
                        if v and v != '${FMODE_API_KEY}': return v
    except: pass
    for p in ['/opt/data/.env','.env']:
        try:
            with open(p,encoding='utf-8') as f:
                for l in f:
                    if 'FMODE_API_KEY' in l:
                        v = l.split('=',1)[1].strip().strip('"\'')
                        if v and '***' not in v and len(v)>10: return v
        except: pass
    print('No API Key found. Set FMODE_API_KEY env or ~/.fmode/config.json')
    sys.exit(1)

def _call_api(prompt, size):
    body = json.dumps({"model":"gpt-image-2.5-sunburst","prompt":prompt,"n":1,"size":size}).encode()
    req = urllib.request.Request(API,data=body,
        headers={"Authorization":f"Bearer {_get_key()}","Content-Type":"application/json"},method='POST')
    resp = urllib.request.urlopen(req,timeout=300)
    data = json.loads(resp.read())
    if 'b64_json' in data['data'][0]: return base64.b64decode(data['data'][0]['b64_json'])
    if 'url' in data['data'][0]: return urllib.request.urlopen(data['data'][0]['url'],timeout=60).read()
    raise Exception('No image data')

def gen(mode, prompt, name='output'):
    cfg = MODES.get(mode)
    if not cfg: print(f'Unknown mode {mode}'); sys.exit(1)
    full = f'{cfg["prefix"]}{prompt} {cfg["suffix"]}'
    outdir = os.environ.get('SKILL_IMAGE_OUTPUT','.')
    os.makedirs(outdir,exist_ok=True)
    path = os.path.join(outdir,f'{name}.png')
    data = _call_api(full,cfg['size'])
    with open(path,'wb') as f: f.write(data)
    sz = os.path.getsize(path)//1024
    print(f'OK {cfg["desc"]} {sz}KB {cfg["size"]} {path}')
    return path

gen_arch=lambda p,n='arch':gen('--arch',p,n)
gen_app=lambda p,n='app':gen('--app',p,n)
gen_explode=lambda p,n='explode':gen('--explode',p,n)
gen_scene=lambda p,n='scene':gen('--scene',p,n)
gen_detail=lambda p,n='detail':gen('--detail',p,n)
gen_slide=lambda p,n='slide':gen('--slide',p,n)

if __name__=='__main__':
    if len(sys.argv)<3: print(__doc__); sys.exit(1)
    mode,content=sys.argv[1],sys.argv[2]
    name=sys.argv[3] if len(sys.argv)>3 else 'output'
    gen(mode,content,name)
