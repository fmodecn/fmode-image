---
name: fmode-image
description: "触发词:生成架构图/场景图/插图。走API出白底PNG，自动读Key，¥0.3-0.5/张。"
version: 2.0.0
author: Fmode
license: MIT
platforms: [linux, macos, windows]
---

# fmode-image v2.0 — AI图像生成器

6种模式 · 零依赖纯ESM · 自动读API Key · 白底PNG直接放PPT

## 六种模式速查

| 模式 | 尺寸 | 成本 | 用途 |
|------|------|------|------|
| `--app` | 1792×1024 | ¥0.5 | **应用界面**（投入产出比最高） |
| `--arch` | 1792×1024 | ¥0.5 | 架构图/分层/闭环 |
| `--slide` | 1920×1080 | ¥0.5 | 整页PPT（封面/金句页） |
| `--explode` | 1792×1024 | ¥0.5 | 爆炸图/内部运转 |
| `--scene` | 1024×1024 | ¥0.3 | 场景插图/痛点 |
| `--detail` | 1024×1024 | ¥0.3 | 零件/材质特写 |

## 安装
```bash
npm install -g fmode-image
```

## 快速使用
```bash
# 应用界面（推荐！）
npx fmode-image --app "标题"内容合规系统"左侧导航5项，顶部指标卡3张" app-demo

# 架构图
npx fmode-image --arch "Harness五层引擎，从上到下数据流" harness

# 场景插图（省40%成本）
npx fmode-image --scene "法务团队深夜加班堆满稿件" scene

# 整页PPT
npx fmode-image --slide "封面：内容营销的超级预审Agent" cover
```

## 输出控制
- `FMODE_API_KEY` 环境变量（必设）
- `SKILL_IMAGE_OUTPUT` 输出目录（默认当前目录）

## 最佳实践
- **--app 界面图**：结构=左导航+顶部指标卡+中间表格+右侧详情，指标卡带同比↑瞬间真实
- **--arch 架构图**：右侧数据卡是灵魂，所有数字必须与讲稿一致
- **--scene 场景图**：给情绪词（焦虑/惊喜）比纯描述生动十倍
- **--slide 整页PPT**：封面/金句/章节过渡页最稳（文字少），内容页素材图+HTML排版

## 独立调用（ESM import）
```js
import { gen, genArch, genApp, genScene, batch } from 'fmode-image';
await genApp('内容营销预审Agent界面', 'my-app');
```

## 链接
- GitHub：https://github.com/fmodecn/fmode-image
- npm：https://www.npmjs.com/package/fmode-image
