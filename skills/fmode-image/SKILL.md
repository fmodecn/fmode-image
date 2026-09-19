---
name: fmode-image
description: "触发词:生成架构图/场景图/插图。走API出白底PNG，自动读Key，¥0.3-0.5/张。"
version: 1.0.0
author: Fmode
license: MIT
platforms: [linux, macos, windows]
---

# fmode-image — AI架构图和场景插图生成器

## 凭据自动获取
自动读取：FMODE_API_KEY (env) → ~/.fmode/config.json → ~/.fmode/config.yaml → .env

## 双模式

### --arch 架构图
- **尺寸**: 1792×1024 (PPT横版)
- **成本**: ≈¥0.5/张
- **风格**: 纯白底、扁平、商务

### --scene 场景/插图
- **尺寸**: 1024×1024 (方形)
- **成本**: ≈¥0.3/张 (省40%)
- **风格**: 扁平插画、清新明亮

## 用法
```bash
# 架构图
npx fmode-image --arch "内容营销预审Agent Harness架构，五层..." case01

# 场景图
npx fmode-image --scene "法务团队被稿件淹没的场景" legal-scene
```

## 独立脚本
scripts/gen.py 可直接运行，不依赖node：python3 gen.py --arch "..." out
