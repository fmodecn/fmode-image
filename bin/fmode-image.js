#!/usr/bin/env node
const path = require('path');
const { spawnSync } = require('child_process');
const GEN = path.resolve(__dirname, '..', 'scripts', 'gen.py');
const args = process.argv.slice(2);
if (!args.length || args[0]==='--help') {
  console.log(`fmode-image — AI架构图和场景插图生成器

用法:
  npx fmode-image --arch    "prompt" [name]    架构图 ¥0.5
  npx fmode-image --app     "prompt" [name]    应用界面 ¥0.5
  npx fmode-image --explode "prompt" [name]    爆炸图 ¥0.5
  npx fmode-image --scene   "prompt" [name]    场景插图 ¥0.3
  npx fmode-image --detail  "prompt" [name]    细节图 ¥0.3
  npx fmode-image --slide   "prompt" [name]    整页PPT ¥0.5

自动读取 FMODE_API_KEY (env/config.json/.env)
输出目录: SKILL_IMAGE_OUTPUT 环境变量控制（默认当前目录）
`);
  process.exit(0);
}
const python = process.platform==='win32'?'python':'python3';
const r = spawnSync(python, [GEN, ...args], { stdio: 'inherit', shell: false });
process.exit(r.status??0);
