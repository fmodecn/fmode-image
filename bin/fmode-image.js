#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');
const lib = path.resolve(__dirname, '..', 'lib', 'fmode-image.mjs');
const args = process.argv.slice(2);
if (!args.length || args[0] === '--help' || args[0] === '-h') {
  console.log('fmode-image v2.0 - AI Architecture & Scene Image Generator');
  console.log('');
  console.log('Usage:');
  console.log('  npx fmode-image --arch    "prompt"  Architecture Diagram  ¥0.5');
  console.log('  npx fmode-image --app     "prompt"  App Interface         ¥0.5');
  console.log('  npx fmode-image --scene   "prompt"  Scene Illustration    ¥0.3');
  console.log('  npx fmode-image --slide   "prompt"  Full Slide            ¥0.5');
  process.exit(0);
}
const r = spawnSync(process.execPath, [lib, ...args], { stdio: 'inherit' });
process.exit(r.status ?? 0);
