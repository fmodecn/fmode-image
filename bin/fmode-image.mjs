#!/usr/bin/env node
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { spawn } from 'node:child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const libPath = join(__dirname, '..', 'lib', 'fmode-image.mjs');

const args = process.argv.slice(2);
if (!args.length || args[0] === '--help' || args[0] === '-h') {
  const { MODES } = await import(libPath);
  console.log(`
fmode-image v2.0 — AI架构图和场景插图生成器

用法:
  npx fmode-image --arch    "prompt" [name]    架构图 ¥0.5
  npx fmode-image --app     "prompt" [name]    应用界面 ¥0.5
  npx fmode-image --scene   "prompt" [name]    场景插图 ¥0.3
  npx fmode-image --slide   "prompt" [name]    整页PPT ¥0.5
  npx fmode-image --explode "prompt" [name]    爆炸图 ¥0.5
  npx fmode-image --detail  "prompt" [name]    细节图 ¥0.3

可用模式:`);
  for (const [m, c] of Object.entries(MODES)) {
    console.log(`  ${m.padEnd(12)} ${c.size.padEnd(14)} ¥${c.cost.toFixed(1)}  ${c.desc}`);
  }
  console.log(`\n环境变量: FMODE_API_KEY(必设), SKILL_IMAGE_OUTPUT(默认当前目录)`);
  process.exit(0);
}

const child = spawn(process.execPath, [libPath, ...args], { stdio: 'inherit', shell: false });
child.on('exit', (code) => process.exit(code ?? 0));
