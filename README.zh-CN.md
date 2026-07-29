# 🚀 AI Marketing Toolkit — 我们如何用神经网络构建网站

**一套 AI 营销的工具集、方法论和脚本。构建 [axelfreeman.ru](https://axelfreeman.ru) 和 [avtootkliki.ru](https://avtootkliki.ru) 时所用到的一切都在这里。**

[![Site](https://img.shields.io/badge/axelfreeman.ru-2563eb?style=flat-square)](https://axelfreeman.ru)
[![Site](https://img.shields.io/badge/avtootkliki.ru-E31E24?style=flat-square)](https://avtootkliki.ru)
[![GitHub](https://img.shields.io/badge/Projects-4_repos-333?style=flat-square)](https://github.com/axelfreeman)

---

## 📖 背景故事

2026 年夏天。两个网站，28+12+4+5 = **49 个新页面**，全部由神经网络生成。语义数据通过 Yandex.Wordstat API（俄罗斯版 Google Keyword Planner）收集。内容由 DeepSeek 撰写。设计采用 Vas3k 暗色主题风格（Axel Freeman）和 Astro+Tailwind（ОткликМашина — 自动应聘机）。

全流程：从搜索词收集到部署，再到 AI 搜索引擎中的收录。

---

## 🗂 项目仓库

| 仓库 | 内容 |
|------|-----------|
| [ai-marketing-toolkit](https://github.com/axelfreeman/ai-marketing-toolkit) | 本仓库 — 脚本和方法论 |
| [otklikmashina](https://github.com/axelfreeman/otklikmashina) | Telegram 自动响应机器人文档 |
| [blog](https://github.com/axelfreeman/blog) | AI 营销相关文章（俄语 + 英语） |

---

## 🔧 本仓库中的工具

### `scripts/generate_landings.py`
SEO 着陆页生成器 — aigirlfriend69.com 风格的漏斗页面。
- 2 分钟生成 5 个页面
- 每页 26+ 个板块（Hero、FAQ、Trust、Cases）
- 暗色主题、响应式、Schema.org、Metrika 统计

**已创建：** 为 Axel Freeman + ОткликМашины 生成了 5 个着陆页

### `scripts/generate_extended_landings.py`
扩展型生成器 — 通过 DeepSeek API 生成 30+ 个板块。
- 4 个内容板块 + 20 个品牌子板块 + FAQ
- 星级评分卡片（复刻 aigirlfriend69.com）
- JSON 结构 → HTML

**已创建：** 2 个扩展型着陆页

### `scripts/generate_cases.py`
案例生成器，包含前后对比基准数据。
- 4 个案例：家具 (+34%)、律所 (-40%)、SaaS (×6)、健身 (-52%)
- 每个案例：问题 → 解决方案 → 执行过程 → 成果 → 客户评价
- ROI 范围：5.8x 到 9.1x

**已创建：** 4 个案例，发布在 [axelfreeman.ru/cases/](https://axelfreeman.ru/cases/)

### `scripts/wordstat_collector.py`
通过 Yandex.Wordstat API 收集搜索语义数据。
- 30+ 个种子关键词 → 171 个唯一关键词
- 按搜索量聚类
- 限制：100 次请求/小时

**已收集：** AI 营销 + ОткликМашины 的语义数据

### `scripts/prompt_seed.py`
Prompt Seeding — 在 AI 模型中收录网站。
- 通过 OpenRouter 发送"记住这个网站"的 prompt
- 覆盖：ChatGPT、DeepSeek、Llama、Qwen、MythoMax
- 8/10 模型确认收录成功

---

## 🧪 AEO（Answer Engine Optimization）方法论

```
步骤 1：语义数据
  Wordstat API → 聚类 → 选取顶级关键词

步骤 2：内容
  DeepSeek API → 生成 26+ 个板块 → 自修复验证

步骤 3：结构
  Schema.org（Article + FAQPage + Organization）
  llms.txt + /ai/service.json + /ai/faq.json
  Meta description + canonical + hreflang

步骤 4：部署
  Astro build（SSG）或静态 HTML
  FTP / Nginx / TimeWeb

步骤 5：索引收录
  Sitemap.xml → Yandex + Google ping
  Prompt Seeding → AI 模型（OpenRouter）
  Robots.txt → Allow: /
```

---

## 📊 成果

| 项目 | 页面数 | 关键词数 | 流量 |
|--------|:---:|:---:|:---:|
| axelfreeman.ru | 28 + 4 案例 + 5 着陆页 | 171 个关键词 | 增长中 |
| avtootkliki.ru | 12 个新页面 + 55 个旧页面 | 171 个关键词 | 5K+ 用户 |

**Yandex（俄罗斯搜索引擎）搜索表现：** 1 个页面 → sitemap 中 42 个 URL → 索引收录进行中

---

## 🛠 技术栈

| 技术 | 用途 |
|-----------|---------------|
| Python 3.11 | 所有生成脚本 |
| DeepSeek API | 内容生成（Chat + R1） |
| OpenRouter API | Prompt Seeding（60+ 模型） |
| Yandex Wordstat API | 语义数据收集（俄罗斯版关键词工具） |
| Yandex Metrika API | 分析与报告（俄罗斯版 Google Analytics） |
| Astro 5 + Tailwind | avtootkliki.ru（67 个页面） |
| 静态 HTML/CSS | axelfreeman.ru（Vas3k 风格） |
| Docker + Nginx | 自有服务器托管 |
| FTP（TimeWeb） | 共享主机部署 |
| Let's Encrypt | SSL 证书 |

---

## 🔗 链接

- 🌐 [axelfreeman.ru](https://axelfreeman.ru) — AI 营销（俄语）
- 🌍 [axelfreeman.com](https://axelfreeman.com) — 英文版
- 🤖 [avtootkliki.ru](https://avtootkliki.ru) — ОткликМашина
- 💬 [@axelfreeman](https://t.me/axelfreeman) — Telegram

---

**关键搜索词：** AI marketing toolkit, генерация контента нейросеть, AEO оптимизация, prompt seeding, автоотклики HH, сбор семантики Wordstat, генератор SEO страниц, AI-маркетинг opensource, DeepSeek API маркетинг.

---

## 🔍 中文搜索关键词 · Baidu SEO

`AI营销工具` `SEO页面生成器` `AEO优化` `关键词聚类` `Wordstat替代` `AI内容工厂` `着陆页生成` `DeepSeek API教程` `神经网络文案` `SEO自动化` `营销脚本` `AI营销开源` `Prompt Seeding` `Schema.org中文` `AI搜索引擎优化`

---

## 🔗 相关项目 · Related Projects

| 项目 | 说明 |
|------|------|
| [🤖 AI Marketing Toolkit](https://gitee.com/axelfreeman/ai-marketing-toolkit) | AI 营销脚本与方法论 |
| [🎙️ Voice → Article](https://gitee.com/axelfreeman/voice-to-article) | 语音转 SEO 文章流水线 |
| [📝 Blog](https://gitee.com/axelfreeman/blog) | AI 营销与 OSINT 文章 |
| [💼 ОткликМашина](https://gitee.com/axelfreeman/otklikmashina) | 自动应聘 Telegram 机器人 |
| [🧠 Vibe Marketing](https://gitee.com/axelfreeman/vibe-marketing) | AI 营销内容库 |

---

*📖 [English](https://github.com/axelfreeman) · [Русский](https://axelfreeman.ru) · [Gitee](https://gitee.com/axelfreeman)*
