#!/usr/bin/env node
const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');

const SKILL_NAME = 'fmode-image';
const SOURCE_ROOT = path.resolve(__dirname, '..');
const SKILL_SOURCE = path.join(SOURCE_ROOT, 'skills', SKILL_NAME);
const GEN_SCRIPT = path.join(SKILL_SOURCE, 'scripts', 'gen.py');
const WORKSPACE_ROOT = process.cwd();

function runGen(passthrough) {
  const python = process.platform === 'win32' ? 'python' : 'python3';
  const result = spawnSync(python, [GEN_SCRIPT, ...passthrough], { stdio: 'inherit', shell: false });
  if (result.error) {
    console.error(`fmode-image: failed to launch generator: ${result.error.message}`);
    process.exit(1);
  }
  process.exit(result.status ?? 0);
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log(`fmode-image — Fmode Image Generator

用法:
  npx fmode-image --arch "prompt" [name]     生成架构图 (1792x1024, ¥0.5)
  npx fmode-image --scene "prompt" [name]    生成场景图 (1024x1024, ¥0.3)

示例:
  npx fmode-image --arch "内容营销预审Agent Harness架构，五层..." case01
  npx fmode-image --scene "法务团队被稿件淹没的办公场景" legal-scene

自动读取 FMODE_API_KEY (env/.fmode/config.json/.env)
`);
  process.exit(0);
}
runGen(args);
