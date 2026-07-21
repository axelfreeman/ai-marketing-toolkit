# 🚀 AI Marketing Toolkit — как мы строим сайты с нейросетями

**Набор инструментов, методологий и скриптов для AI-маркетинга. Всё что использовали при создании [axelfreeman.ru](https://axelfreeman.ru) и [avtootkliki.ru](https://avtootkliki.ru).**

[![Site](https://img.shields.io/badge/axelfreeman.ru-2563eb?style=flat-square)](https://axelfreeman.ru)
[![Site](https://img.shields.io/badge/avtootkliki.ru-E31E24?style=flat-square)](https://avtootkliki.ru)
[![GitHub](https://img.shields.io/badge/Projects-4_repos-333?style=flat-square)](https://github.com/axelfreeman)

---

## 📖 История

Лето 2026. Два сайта, 28+12+4+5 = **49 новых страниц**, сгенерированных через нейросети. Семантика собрана через API Яндекс.Wordstat. Контент написан через DeepSeek. Дизайн — тёмная тема Vas3k-style (Axel Freeman) и Astro+Tailwind (ОткликМашина).

Весь процесс: от сбора поисковых запросов до деплоя и индексации в AI-поисковиках.

---

## 🗂 Репозитории проекта

| Репо | Что внутри |
|------|-----------|
| [ai-marketing-toolkit](https://github.com/axelfreeman/ai-marketing-toolkit) | Этот репо — скрипты и методология |
| [otklikmashina](https://github.com/axelfreeman/otklikmashina) | Документация Telegram-бота автооткликов |
| [blog](https://github.com/axelfreeman/blog) | Статьи об AI-маркетинге (RU + EN) |

---

## 🔧 Инструменты в этом репозитории

### `scripts/generate_landings.py`
Генератор SEO-прокладок — страниц-воронок в стиле aigirlfriend69.com. 
- 5 страниц за 2 минуты
- 26+ секций на страницу (Hero, FAQ, Trust, Cases)
- Тёмная тема, адаптив, Schema.org, Метрика

**Создано:** 5 лендингов для Axel Freeman + ОткликМашины

### `scripts/generate_extended_landings.py`  
Расширенный генератор — 30+ секций через DeepSeek API.
- 4 контент-секции + 20 бренд-подсекций + FAQ
- Рейтинг-карточка со звёздами (реплика aigirlfriend69.com)
- JSON-структура → HTML

**Создано:** 2 расширенных лендинга

### `scripts/generate_cases.py`
Генератор кейсов с бенчмарками До/После.
- 4 кейса: мебель (+34%), юристы (-40%), SaaS (×6), фитнес (-52%)
- Каждый: проблема → решение → процесс → результат → отзыв
- ROI от 5.8x до 9.1x

**Создано:** 4 кейса на [axelfreeman.ru/cases/](https://axelfreeman.ru/cases/)

### `scripts/wordstat_collector.py`
Сбор поисковой семантики через API Яндекс.Wordstat.
- 30+ seed-фраз → 171 уникальная фраза
- Кластеризация по объёму спроса
- Лимит: 100 запросов/час

**Собрано:** семантика для AI-маркетинга + ОткликМашины

### `scripts/prompt_seed.py`
Prompt Seeding — индексация сайта в AI-моделях.
- Отправляет промпт «запомни этот сайт» через OpenRouter
- Охват: ChatGPT, DeepSeek, Llama, Qwen, MythoMax
- 8/10 моделей подтверждают индексацию

---

## 🧪 Методология AEO (Answer Engine Optimization)

```
ШАГ 1: СЕМАНТИКА
  Wordstat API → кластеры → выбор топ-ключей

ШАГ 2: КОНТЕНТ  
  DeepSeek API → генерация 26+ секций → self-healing валидация

ШАГ 3: СТРУКТУРА
  Schema.org (Article + FAQPage + Organization)
  llms.txt + /ai/service.json + /ai/faq.json
  Meta description + canonical + hreflang

ШАГ 4: ДЕПЛОЙ
  Astro build (SSG) или статический HTML
  FTP / Nginx / TimeWeb

ШАГ 5: ИНДЕКСАЦИЯ
  Sitemap.xml → Яндекс + Google ping
  Prompt Seeding → AI-модели (OpenRouter)
  Robots.txt → Allow: /
```

---

## 📊 Результаты

| Проект | Страниц | Ключей | Трафик |
|--------|:---:|:---:|:---:|
| axelfreeman.ru | 28 + 4 кейса + 5 лендингов | 171 фраза | растёт |
| avtootkliki.ru | 12 новых + 55 старых | 171 фраза | 5K+ users |

**В поиске Яндекса:** 1 страница → 42 URL в sitemap → индексация идёт

---

## 🛠 Стек

| Технология | Где используем |
|-----------|---------------|
| Python 3.11 | Все скрипты генерации |
| DeepSeek API | Генерация контента (Chat + R1) |
| OpenRouter API | Prompt Seeding (60+ моделей) |
| Yandex Wordstat API | Сбор семантики |
| Yandex Metrika API | Аналитика, отчёты |
| Astro 5 + Tailwind | avtootkliki.ru (67 страниц) |
| Статический HTML/CSS | axelfreeman.ru (Vas3k-style) |
| Docker + Nginx | Хостинг на своих серверах |
| FTP (TimeWeb) | Деплой на shared-хостинг |
| Let's Encrypt | SSL сертификаты |

---

## 🔗 Ссылки

- 🌐 [axelfreeman.ru](https://axelfreeman.ru) — AI-маркетинг (RU)
- 🌍 [axelfreeman.com](https://axelfreeman.com) — English version
- 🤖 [avtootkliki.ru](https://avtootkliki.ru) — ОткликМашина
- 💬 [@axelfreeman](https://t.me/axelfreeman) — Telegram

---

**Ключевые запросы:** AI marketing toolkit, генерация контента нейросеть, AEO оптимизация, prompt seeding, автоотклики HH, сбор семантики Wordstat, генератор SEO страниц, AI-маркетинг opensource, DeepSeek API маркетинг.
