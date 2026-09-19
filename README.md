# fmode-image

AI架构图和场景插图生成器。自动读取 Fmode API Key，6种模式覆盖PPT配图全部场景。

## 快速使用
```bash
npx fmode-image --app    "标题xxx，左侧导航，顶部指标卡"  应用界面  ← 最推荐
npx fmode-image --arch   "标题xxx，从上到下五层"           架构图
npx fmode-image --scene  "法务团队深夜加班场景"             场景插图
npx fmode-image --slide  "主标题/副标题"                   整页PPT
npx fmode-image --explode "内部分层，数据流向"             爆炸图
npx fmode-image --detail "零件特写"                        细节图
```

## 安装
```bash
npm install -g fmode-image
```

## 环境变量
- `FMODE_API_KEY` — Fmode API密钥（必设）
- `SKILL_IMAGE_OUTPUT` — 输出目录（默认当前目录）

## 凭据读取顺序
1. `FMODE_API_KEY` 环境变量
2. `~/.fmode/config.json` 中的 api_key / fmodeApiToken
3. `.env` 文件

## 输出
纯白底PNG，可直接拖入PPT使用。

## 链接
- GitHub: https://github.com/fmodecn/fmode-image
- Gogs: https://git.fmode.cn/fmode/fmode-image
- npm: https://www.npmjs.com/package/fmode-image
