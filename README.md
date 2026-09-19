# fmode-image

AI架构图和场景插图生成器。自动读取 Fmode API Key，支持架构图和场景图双模式。

## 快速使用
```bash
npx fmode-image --arch "你的架构图描述" 输出文件名
npx fmode-image --scene "你的场景描述" 输出文件名
```

## 安装
```bash
npm install -g fmode-image
```

## 环境变量
- `FMODE_API_KEY` — Fmode API 密钥
- `SKILL_IMAGE_OUTPUT` — 输出目录 (默认当前目录)
