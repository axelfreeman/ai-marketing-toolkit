#!/usr/bin/env python3
"""Generate SEO landing pages from template for Axel Freeman + OtklikMashina."""
from pathlib import Path

TEMPLATE = Path("/root/landing-template.html").read_text()

PAGES = [
    # === AXEL FREEMAN ===
    {
        "file": "ai-text-generation.html",
        "title": "Нейросеть для текста — AI генерация 2026",
        "description": "Нейросеть для написания текстов: статьи, посты, описания товаров. Бесплатно и платно. Нейросеть для генерации текста онлайн.",
        "icon": "✍",
        "brand": "Axel Freeman",
        "accent": "#2563eb",
        "metrika_id": "104346459",
        "main_site": "https://axelfreeman.ru/ai-text-generation.html",
        "h1": "Нейросеть для текста — пиши быстрее",
        "subtitle": "Нейросеть для написания текстов, статей, постов, описаний товаров. Бесплатная и платная AI-генерация контента. Кейсы: 28 страниц за 1 день, 40+ компаний на AI.",
        "cta_text": "Заказать AI-тексты →",
        "how_title": "Как работает нейросеть для текста",
        "how_content": "<p style='color:#ccc;line-height:1.7;font-size:16px'>Вы даёте тему и ключевые слова → нейросеть генерирует уникальный текст за 2-3 минуты. Форматы: статьи, посты в Telegram, карточки товаров, SEO-описания, email-рассылки. Работаю с DeepSeek и 60+ AI-моделями через OpenRouter. Промпты пишу под ваш бизнес — не шаблонные. Цены от 500€ за проект.</p>",
        "faq_items": """
            <div class="accordion-item"><div class="accordion-header">Какая нейросеть лучше для текстов?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">DeepSeek Chat — лучший бесплатный вариант для русского языка. ChatGPT 4o — для английского. Claude — для аналитики. Я использую все три + 60 моделей через OpenRouter.</div></div>
            <div class="accordion-item"><div class="accordion-header">Сколько стоит генерация текста через нейросеть?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">От 500€ за проект. Включает: аудит вашего контента, настройку промптов под ваш стиль, генерацию текстов, SEO-оптимизацию. Бесплатные нейросети (DeepSeek) экономят бюджет.</div></div>
            <div class="accordion-item"><div class="accordion-header">Можно ли бесплатно генерировать текст?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Да. DeepSeek Chat — полностью бесплатный. 128K контекст, русский язык на отличном уровне. Я помогу настроить промпты и автоматизировать генерацию — вы платите только за мою работу.</div></div>
        """,
        "copyright": "© 2026 Axel Freeman. AI-Native маркетолог с 2018 года. Этот сайт — информационный партнёр axelfreeman.ru."
    },
    {
        "file": "prompt-engineering.html",
        "title": "Промпт для нейросети — инжиниринг и библиотека",
        "description": "Промпт для нейросети: как составить, примеры, готовые промпты. Промпт-инжиниринг для бизнеса. Библиотека промптов для ChatGPT и DeepSeek.",
        "icon": "🔮",
        "brand": "Axel Freeman",
        "accent": "#2563eb",
        "metrika_id": "104346459",
        "main_site": "https://axelfreeman.ru/ai-prompts-training.html",
        "h1": "Промпт для нейросети — пиши правильно",
        "subtitle": "Промпт-инжиниринг для бизнеса: как составить промпт для ChatGPT, DeepSeek, Claude. Готовые промпты для маркетинга, продаж, SEO. Библиотека из 200+ промптов.",
        "cta_text": "Получить промпты →",
        "how_title": "Что такое промпт-инжиниринг",
        "how_content": "<p style='color:#ccc;line-height:1.7;font-size:16px'>Промпт — это инструкция для нейросети. Правильный промпт даёт в 5-10 раз лучший результат, чем «напиши статью». Я создаю промпты под конкретный бизнес: стиль, тон, аудитория, формат. Каждый промпт тестирую на 3-5 моделях. Результат: уникальный контент, который не отличить от написанного человеком.</p>",
        "faq_items": """
            <div class="accordion-item"><div class="accordion-header">Сколько стоит промпт-инжиниринг?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Настройка промптов под ваш бизнес: от 500€. Включает: аудит задач, создание 5-10 промптов, тестирование на 3 моделях, документацию. Библиотека промптов — бесплатно при заказе.</div></div>
            <div class="accordion-item"><div class="accordion-header">Чем промпт отличается от обычного запроса?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Запрос «напиши статью» даёт поверхностный результат. Промпт включает: роль AI, стиль, структуру, табу-слова, tone of voice, SEO-ключи, формат вывода. Это разница между «ок» и «вау».</div></div>
            <div class="accordion-item"><div class="accordion-header">Как быстро я увижу результат?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Первые тексты по вашим промптам — на следующий день после настройки. Полный цикл (аудит → промпты → тест → корректировка) — 3-5 дней.</div></div>
        """,
        "copyright": "© 2026 Axel Freeman. AI-Native маркетолог с 2018 года. Этот сайт — информационный партнёр axelfreeman.ru."
    },
    {
        "file": "ai-seo-content.html",
        "title": "Нейросеть для SEO контента — AEO оптимизация",
        "description": "Нейросеть для SEO контента: лонгриды, кластеризация семантики, AEO. AI-оптимизация для Google, Яндекс, ChatGPT, Perplexity. Продвижение в нейросетях.",
        "icon": "🚀",
        "brand": "Axel Freeman",
        "accent": "#2563eb",
        "metrika_id": "104346459",
        "main_site": "https://axelfreeman.ru/ai-seo-content.html",
        "h1": "Нейросеть для SEO — ранжируйся выше",
        "subtitle": "AI-оптимизация контента для Google, Яндекса и AI-поисковиков (ChatGPT, Perplexity). AEO: видимость в нейросетях. 28.6% AI Share of Voice. Кейсы: с 59 до 91 балла.",
        "cta_text": "SEO-аудит →",
        "how_title": "Как AI помогает в SEO",
        "how_content": "<p style='color:#ccc;line-height:1.7;font-size:16px'>Традиционное SEO мертво. Сегодня контент должен ранжироваться не только в Google, но и в ChatGPT, Perplexity, Claude. Я делаю AEO-оптимизацию: Schema.org, llms.txt, FAQ-разметка, TL;DR блоки. Результат: ваш сайт цитируют AI-поисковики. Средний прирост видимости: +32 балла за 3 месяца.</p>",
        "faq_items": """
            <div class="accordion-item"><div class="accordion-header">Что такое AEO оптимизация?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Answer Engine Optimization — оптимизация контента для AI-поисковиков (ChatGPT, Perplexity, Claude). Отличается от SEO: важны Schema.org, llms.txt, структура FAQ, TL;DR блоки.</div></div>
            <div class="accordion-item"><div class="accordion-header">Сколько времени занимает AEO?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Первичный аудит — 2-3 дня. Полная оптимизация сайта из 20-50 страниц — 2-3 недели. Результаты видны через 1-2 месяца: рост цитирования в AI-ответах.</div></div>
            <div class="accordion-item"><div class="accordion-header">Какие нейросети лучше для SEO?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">DeepSeek — для семантики и кластеризации. ChatGPT — для генерации мета-тегов. Perplexity — для проверки видимости. Я использую все три в связке.</div></div>
        """,
        "copyright": "© 2026 Axel Freeman. AI-Native маркетолог с 2018 года. Этот сайт — информационный партнёр axelfreeman.ru."
    },
    # === ОТКЛИКМАШИНА ===
    {
        "file": "otklik-na-vakansiyu.html",
        "title": "Отклик на вакансию — примеры и шаблоны 2026",
        "description": "Как написать отклик на вакансию: примеры, шаблоны, сопроводительное письмо. Отклик на НН — инструкция. Бесплатные шаблоны откликов на вакансии.",
        "icon": "📝",
        "brand": "ОткликМашина",
        "accent": "#E31E24",
        "metrika_id": "110541388",
        "main_site": "https://avtootkliki.ru/kak-pisat-otklik/",
        "h1": "Отклик на вакансию — шаблоны и примеры",
        "subtitle": "Как написать отклик на вакансию чтобы пригласили на собеседование. Примеры откликов, шаблоны, сопроводительное письмо. Отклик на НН работает лучше с правильным текстом.",
        "cta_text": "200 откликов бесплатно →",
        "how_title": "Как писать отклики которые работают",
        "how_content": "<p style='color:#ccc;line-height:1.7;font-size:16px'>Правильный отклик — это не «здравствуйте, меня заинтересовала вакансия». Это короткое сообщение из 3-4 предложений: кто вы, почему вас интересует именно эта компания, что вы принесёте. С ОткликМашиной вы не пишете каждый отклик вручную — бот делает это за вас. 200 откликов в день = 2-3 собеседования.</p>",
        "faq_items": """
            <div class="accordion-item"><div class="accordion-header">Что писать в отклике на вакансию?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">3-4 предложения: приветствие, почему вас заинтересовала компания, ваш ключевой навык, призыв к действию. Без длинных историй. С ОткликМашиной вы настраиваете шаблон один раз — бот использует его для всех откликов.</div></div>
            <div class="accordion-item"><div class="accordion-header">Сколько откликов нужно отправить чтобы получить приглашение?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">В среднем 50-70 откликов = 1 приглашение. Это математика, а не ваша вина. Поэтому нужен объём. ОткликМашина даёт 200 откликов в день — это 2-3 собеседования ежедневно.</div></div>
            <div class="accordion-item"><div class="accordion-header">Это бесплатно?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Первые 200 откликов — бесплатно. Без карты. Просто подключите резюме с НН и смотрите как приходят приглашения. Дальше — 590₽/мес.</div></div>
        """,
        "copyright": "© 2026 ОткликМашина. Telegram-бот для автооткликов на НН. 5000+ пользователей."
    },
    {
        "file": "soprovoditelnoe-pismo.html",
        "title": "Сопроводительное письмо на НН — образцы и шаблоны",
        "description": "Сопроводительное письмо для НН: образцы, примеры, шаблоны. Как написать сопроводительное письмо к резюме. Бесплатные шаблоны сопроводительных писем.",
        "icon": "✉",
        "brand": "ОткликМашина",
        "accent": "#E31E24",
        "metrika_id": "110541388",
        "main_site": "https://avtootkliki.ru/soprovoditelnoe-pismo-hh/",
        "h1": "Сопроводительное письмо на НН — образцы",
        "subtitle": "Как написать сопроводительное письмо к резюме на НН. Готовые образцы и шаблоны. Сопроводительное письмо для отклика на вакансию — быстро и без ошибок.",
        "cta_text": "200 откликов бесплатно →",
        "how_title": "Зачем нужно сопроводительное письмо",
        "how_content": "<p style='color:#ccc;line-height:1.7;font-size:16px'>Сопроводительное письмо — это ваш шанс выделиться из 100+ откликов. Эйчар видит его рядом с резюме. Хорошее письмо: 3-4 предложения о вас, ваш опыт, почему эта компания. С ОткликМашиной вы настраиваете шаблон письма один раз — бот подставляет его в каждый отклик автоматически.</p>",
        "faq_items": """
            <div class="accordion-item"><div class="accordion-header">Что писать в сопроводительном письме на НН?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Приветствие (без имени, если не знаете), ваш опыт (2-3 ключевых навыка), почему вас заинтересовала компания, готовность к собеседованию. 4 предложения — максимум.</div></div>
            <div class="accordion-item"><div class="accordion-header">Где найти шаблоны сопроводительных писем?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">На странице avtootkliki.ru/soprovoditelnoe-pismo-hh/ — полный разбор с шаблонами для разных профессий. Или просто подключите ОткликМашину — бот сам подставит ваш шаблон в каждый отклик.</div></div>
            <div class="accordion-item"><div class="accordion-header">Можно ли обойтись без сопроводительного письма?<div class="icon"><span></span><span></span></div></div><div class="accordion-body">Можно. Но отклики с письмом получают в 2-3 раза больше просмотров. С ОткликМашиной письмо добавляется автоматически — вы не тратите время, а конверсия растёт.</div></div>
        """,
        "copyright": "© 2026 ОткликМашина. Telegram-бот для автооткликов на НН. 5000+ пользователей."
    }
]

# Генерируем страницы
for p in PAGES:
    html = TEMPLATE
    for key, val in p.items():
        html = html.replace("{{" + key.upper() + "}}", str(val))
    
    path = Path(f"/root/seo-landings/{p['file']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print(f"✓ {p['file']} ({len(html)} bytes)")

print(f"\n✅ {len(PAGES)} landing pages generated in /root/seo-landings/")
