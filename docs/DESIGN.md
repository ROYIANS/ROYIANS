# ROYIANS Profile · 设计与维护

这是 GitHub 个人主页 README，发布目标为 `ROYIANS/ROYIANS` 仓库的 `main` 分支。主页面由原生 Markdown、GitHub 支持的 HTML 与本仓库 SVG 图片组成，无需部署网站或安装 Node 依赖。

## 视觉方向

主题为 **A personal workshop / 个人创作工作室**。

- 主标题：**Small ideas. Real things.**
- 浅色：暖纸色、墨黑、苔绿、朱橙，少量灰蓝与明黄。
- 深色：深墨绿底、米白文字、柔和的橙与绿。
- 图形：拱门代表小小的创作空间，纸张呼应 Foliq，声波与播放按钮呼应 Cuepoint，房间呼应 Dicha，分岔道路呼应 TheTwo。
- 主视觉使用 Georgia 衬线字体，辅助标注使用系统等宽字体。图片不依赖外部字体下载。
- 主要内容保留为可选择、可访问的正文，每张图片有替代文本。

所有插画均为本项目原创几何 SVG，不需要 AI 生图。使用 `<picture>` 为深浅配色提供不同资产。不依赖统计卡片、远程徽章服务、脚本、SVG foreignObject 或自定义 README CSS。

## 内容依据

2026-09-22 核对了 GitHub 公开账号信息、原创仓库列表及以下项目的公开 README：

- [Cuepoint](https://github.com/ROYIANS/Cuepoint)：本地优先 AI 创作工作室，视频、音频、音乐项目和自带模型连接。
- [Foliq](https://github.com/ROYIANS/foliq-print-template-designer)：结构化文档设计与确定性 PDF 输出；v2 重写仍在进行。
- [Dicha](https://github.com/ROYIANS/dicha)：个人物品与房间管理；Pre-alpha，像素空间是后续方向。配图为概念插画，不是产品截图。
- [FamiStudio Compose Skill](https://github.com/ROYIANS/famistudio-compose-skill)：NES 芯片音乐创作、结构化编辑、校验和官方工具渲染。
- [TheTwo](https://github.com/ROYIANS/TheTwo)：早期产品设计，尚无可运行版本。
- [Dreamland Book](https://github.com/ROYIANS/hexo-theme-dreamlandbook)：基于 Maple 修改的 Hexo 主题。

按作者确认，精选项目为 Cuepoint、Foliq、Dicha、TheTwo；FamiStudio 移至工作台，Wabi 不展示。图来 · TULAI 使用作者提供的介绍，仅展示公开产品地址 https://tulai.design/，不链接私有仓库。作者确认的博客地址为 https://vidorra.life/，不将它标记为梦岛书主题演示。择途的 https://royians.github.io/TheTwo/ 是概念原型，因此入口明确标注「概念预览」。Dicha 提供 https://dicha.life/ 入口；FamiStudio 提供 Boss Chase 音频文件入口。

自我介绍是一版基于上述项目方向写作的个人文案，可直接调整语气。未写入未经确认的职位、雇主、城市、联系方式或履历。保留原 README 的爱发电地址。

## 修改与预览

修改个人介绍、项目描述与链接：编辑 `README.md`。

修改颜色或插画：编辑 `scripts/generate_assets.py`，然后运行：

```sh
python3 scripts/generate_assets.py
```

生成器只使用 Python 标准库。12 张 SVG 总体积很小，可直接提交。

使用 GitHub Markdown API 生成本地预览（需要联网，会把当前 README 文本发送给 GitHub 渲染）：

```sh
python3 scripts/preview.py
python3 -m http.server 8765 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8765/.preview/`。也可以直接打开 `.preview/index.html`。预览采用 GitHub 返回的 HTML 和 GitHub 风格 CSS；仅外层容器由本地模拟，线上最终效果以 GitHub 为准。

`.preview/` 已忽略，不会随主页提交。发布时提交 `README.md`、`assets/` 及需要保留的维护文件并推送到 `main`，GitHub 即可显示主页，无需 Actions 或 GitHub Pages。

## 版式检查

检查桌面浅色、桌面深色以及 390px 手机宽度：图片应正常加载，深色应选择 `*-dark.svg`，页面与项目表格应无横向溢出。GitHub README 不支持自定义响应式 CSS，因此精选项目采用原生双列表格，手机上仍为两列；下方工作台使用自然换行的列表。
