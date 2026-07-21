#!/usr/bin/env python3
"""Generate extended SEO landings (25+ sections) mimicking aigirlfriend69.com structure."""
import json, re, subprocess, time
from pathlib import Path

ENV = Path("/root/.hermes/profiles/marketing/.env")
KEY = None
if ENV.exists():
    for line in ENV.read_text().splitlines():
        if line.startswith("DEEPSEEK_API_KEY="):
            KEY = line.split("=", 1)[1].strip()

API = "https://api.deepseek.com/v1/chat/completions"

SYSTEM = """Ты создаёшь SEO-лендинг в стиле aigirlfriend69.com — dark theme, структура из 26 секций.

СТРУКТУРА СТРАНИЦЫ (ровно 26 блоков, каждый с заголовком H2 или H3):

1. HERO — H1 заголовок + подзаголовок + CTA кнопка
2-5. 4 БЛОКА КОНТЕНТА — по 80-120 слов с H2 и параграфами
6-25. 20 БЛОКОВ ПРО БРЕНД — H2 с названием бренда + 5 групп по 4 H3 подсекции (всего 20 H3)
26. FAQ — 5 вопросов с ответами

ФОРМАТ ОТВЕТА — строго JSON:
{
  "h1": "Заголовок H1",
  "subtitle": "Подзаголовок под H1 (1-2 предложения)",
  "cta_text": "Текст на кнопке",
  "sections": [
    {"title": "Заголовок H2", "content": "Текст 80-120 слов"},
    ... (4 секции)
  ],
  "brand_h2": "Название бренда H2",
  "brand_subsections": [
    {"title": "Подзаголовок H3", "content": "Текст 60-80 слов"},
    ... (20 подсекций, сгруппированных по 4: True Customization, Multi-Modal, Smooth Chatting, Accessible, Trusted)
  ],
  "faq": [
    {"q": "Вопрос", "a": "Ответ 2-3 предложения"},
    ... (5 вопросов)
  ]
}

Текст должен быть SEO-оптимизирован, с ключевыми словами, на русском языке, без маркетинговых штампов."""

PAGES = [
    {
        "slug": "ai-text",
        "brand": "Axel Freeman",
        "main_url": "https://axelfreeman.ru/ai-text-generation.html",
        "cta_url": "https://axelfreeman.ru/ai-text-generation.html",
        "accent": "#2563eb",
        "metrika": "104346459",
        "topic": "нейросеть для текста и генерации контента",
        "keywords": "нейросеть для текста, нейросеть для генерации текста, AI копирайтинг, написание текстов нейросетью, ChatGPT для текстов, DeepSeek генерация, AI контент",
        "brand_desc": "Axel Freeman — AI-Native маркетолог с 2018 года. 40+ компаний внедрили AI. Специализация: генерация контента через нейросети, AEO-оптимизация, автоматизация маркетинга."
    },
    {
        "slug": "otklik",
        "brand": "ОткликМашина",
        "main_url": "https://avtootkliki.ru/kak-pisat-otklik/",
        "cta_url": "https://t.me/otklikauto_bot",
        "accent": "#E31E24",
        "metrika": "110541388",
        "topic": "отклик на вакансию и автоотклики НН",
        "keywords": "отклик на вакансию, как писать отклик, автоотклики НН, бот для откликов, сопроводительное письмо, быстрый поиск работы",
        "brand_desc": "ОткликМашина — Telegram-бот для автооткликов на НН. 200 откликов в день, 6000 в месяц. 5000+ пользователей, 500 000+ отправленных откликов. Создан в 2024 году."
    }
]

def call_llm(prompt):
    payload = json.dumps({
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.75,
        "max_tokens": 8000
    })
    for attempt in range(3):
        try:
            r = subprocess.run(
                ["curl", "-s", "--max-time", "120", API,
                 "-H", f"Authorization: Bearer {KEY}",
                 "-H", "Content-Type: application/json",
                 "-d", payload],
                capture_output=True, text=True, timeout=130
            )
            data = json.loads(r.stdout)
            if "choices" in data and data["choices"]:
                content = data["choices"][0]["message"]["content"]
                content = re.sub(r'^```[a-z]*\s*', '', content)
                content = re.sub(r'\s*```$', '', content)
                return json.loads(content)
            else:
                print(f"  LLM error: {data.get('error', {}).get('message', 'unknown')[:100]}")
                time.sleep(3)
        except json.JSONDecodeError as e:
            print(f"  JSON decode: {e}")
            time.sleep(3)
    return None

TEMPLATE = Path("/root/landing-extended-template.html").read_text() if Path("/root/landing-extended-template.html").exists() else None

for p in PAGES:
    print(f"\n{'='*60}")
    print(f"Generating: {p['slug']} ({p['brand']})")
    print(f"{'='*60}")
    
    prompt = f"""Создай SEO-лендинг для {p['brand']} на тему: {p['topic']}.

Ключевые слова: {p['keywords']}
Описание бренда: {p['brand_desc']}
Основной сайт: {p['main_url']}

Создай 26 секций по структуре из system prompt. 
4 контент-секции должны объяснять что это за услуга, как работает, преимущества, форматы.
20 подсекций бренда должны детально раскрывать:
- Группа 1 (4 H3): конкретные кейсы с цифрами
- Группа 2 (4 H3): процесс работы и методология
- Группа 3 (4 H3): инструменты, технологии, стек
- Группа 4 (4 H3): цены, тарифы, форматы сотрудничества
- Группа 5 (4 H3): отзывы, гарантии, безопасность, поддержка"""
    
    data = call_llm(prompt)
    if not data:
        print(f"  ❌ Failed to generate")
        continue
    
    # Build HTML
    sections_html = ""
    for s in data.get("sections", []):
        sections_html += f'<h2>{s["title"]}</h2>\n<p>{s["content"]}</p>\n'
    
    # Brand subsections in 5 groups
    subsections = data.get("brand_subsections", [])
    group_names = [
        "Реальные кейсы и результаты",
        "Процесс работы и методология", 
        "Инструменты и технологии",
        "Цены и форматы сотрудничества",
        "Отзывы, гарантии и поддержка"
    ]
    brand_html = f'<h2>{data.get("brand_h2", p["brand"])}</h2>\n'
    for gi, gn in enumerate(group_names):
        start = gi * 4
        end = start + 4
        group = subsections[start:end]
        brand_html += f'<h3>{gn}</h3>\n'
        for s in group:
            brand_html += f'<h4>{s["title"]}</h4>\n<p>{s["content"]}</p>\n'
    
    # FAQ
    faq_html = ""
    for f in data.get("faq", []):
        faq_html += f'''<div class="accordion-item">
            <div class="accordion-header">{f["q"]}<div class="icon"><span></span><span></span></div></div>
            <div class="accordion-body">{f["a"]}</div></div>\n'''
    
    # Rating card (hardcoded stats)
    rating_html = f'''<a href="{p['cta_url']}" target="_blank" class="service-card">
        <div class="service-body">
            <div class="logo">{p['brand']}</div>
            <ul>
                <li>Лучший выбор 2026 по версии пользователей</li>
                <li>{p['brand_desc'][:100]}...</li>
            </ul>
            <div class="rating">
                <div class="rating-container">
                    <div class="num">9.8</div>
                    <div class="desk">
                        <div class="title">Top-rated</div>
                        <div class="stars">
                            <div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div>
                        </div>
                    </div>
                </div>
                <p><b>2,847</b> User Votes</p>
            </div>
            <div class="btn">Перейти на сайт</div>
        </div>
    </a>'''
    
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{data["h1"]}</title>
    <meta name="description" content="{data["subtitle"]}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='28' font-size='28'>🦑</text></svg>">
    <style>
        * {{ font-family: "Figtree", system-ui, sans-serif; margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #0a0a1a; color: #fff; display: flex; flex-direction: column; min-height: 100vh; }}
        main {{ flex: 1; }}
        
        .header-banner {{ background: linear-gradient(90deg, {p['accent']}, {p['accent']}99); color: #fff; display: flex; align-items: center; justify-content: center; gap: 20px; padding: 12px 20px; text-decoration: none; font-size: 14px; font-weight: 600; }}
        .header-banner .btn {{ background: #fff; color: {p['accent']}; padding: 8px 20px; border-radius: 20px; font-weight: 700; }}
        
        header {{ background: #000; height: 60px; position: sticky; top: 0; z-index: 100; }}
        .header-wrapper {{ max-width: 1110px; height: 100%; margin: auto; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; }}
        header .logo {{ font-size: 20px; font-weight: 700; text-decoration: none; color: #fff; }}
        
        .under-header {{ padding: 80px 20px; text-align: center; background: linear-gradient(135deg, #0a0a1a, {p['accent']}20); }}
        .under-header h1 {{ font-size: 48px; max-width: 900px; margin: 0 auto 20px; line-height: 1.2; }}
        .under-header .date {{ color: {p['accent']}; font-size: 14px; margin-bottom: 10px; }}
        .under-header p {{ max-width: 700px; margin: 0 auto 30px; font-size: 16px; color: #ccc; line-height: 1.6; }}
        .under-header .btn {{ background: {p['accent']}; color: #fff; text-decoration: none; padding: 12px 40px; border-radius: 30px; font-weight: 700; font-size: 16px; display: inline-block; }}
        
        .container {{ max-width: 1110px; margin: auto; padding: 0 20px; }}
        
        .service-card {{ display: block; background: #1a1a2e; border: 1px solid {p['accent']}33; border-radius: 16px; padding: 30px; margin: 30px 0; text-decoration: none; color: #fff; transition: 0.3s; }}
        .service-card:hover {{ border-color: {p['accent']}; }}
        .service-body .logo {{ font-size: 28px; font-weight: 900; margin-bottom: 16px; color: {p['accent']}; }}
        .service-body ul {{ list-style: none; margin-bottom: 20px; }}
        .service-body ul li {{ padding: 6px 0; color: #ccc; font-size: 14px; }}
        .service-body ul li::before {{ content: "✓ "; color: {p['accent']}; font-weight: bold; }}
        .rating {{ display: flex; align-items: center; gap: 16px; }}
        .rating .num {{ font-size: 36px; font-weight: 900; color: {p['accent']}; }}
        .stars {{ display: flex; gap: 3px; }}
        .star {{ width: 16px; height: 16px; background: #db8c0a; clip-path: polygon(50% 0%, 63% 38%, 100% 38%, 73% 62%, 82% 100%, 50% 75%, 18% 100%, 27% 62%, 0% 38%, 37% 38%); }}
        .service-body .btn {{ background: {p['accent']}; color: #fff; padding: 10px 30px; border-radius: 25px; display: inline-block; margin-top: 16px; font-weight: 700; }}
        
        article {{ padding: 40px 0; }}
        article h2 {{ font-size: 32px; margin: 40px 0 16px; color: #fff; }}
        article h3 {{ font-size: 24px; margin: 30px 0 12px; color: {p['accent']}; }}
        article h4 {{ font-size: 18px; margin: 20px 0 8px; color: #ddd; }}
        article p {{ font-size: 16px; line-height: 1.7; color: #ccc; margin-bottom: 16px; }}
        
        .faq {{ background: #000; padding: 60px 20px; }}
        .faq h2 {{ font-size: 32px; text-align: center; margin-bottom: 30px; }}
        .accordion {{ max-width: 800px; margin: auto; }}
        .accordion-item {{ margin-top: 12px; }}
        .accordion-header {{ display: flex; align-items: center; justify-content: space-between; background: #1a1a2e; padding: 18px 20px; border-radius: 8px; cursor: pointer; font-size: 18px; font-weight: 600; }}
        .accordion-header .icon {{ position: relative; width: 24px; height: 24px; }}
        .accordion-header .icon span {{ position: absolute; background: #fff; border-radius: 3px; transition: 0.3s; }}
        .accordion-header .icon span:nth-child(1) {{ width: 16px; height: 2px; top: 11px; left: 4px; }}
        .accordion-header .icon span:nth-child(2) {{ width: 2px; height: 16px; top: 4px; left: 11px; }}
        .accordion-item.active .icon span:nth-child(2) {{ opacity: 0; transform: scale(0); }}
        .accordion-body {{ padding: 0 20px; max-height: 0; overflow: hidden; transition: 0.4s; font-size: 16px; line-height: 1.6; color: #ccc; }}
        .accordion-item.active .accordion-body {{ padding: 16px 20px; max-height: 300px; }}
        
        .footer-banner {{ background: linear-gradient(90deg, {p['accent']}, {p['accent']}99); text-align: center; padding: 30px 20px; }}
        .footer-banner p {{ font-size: 24px; font-weight: 700; margin-bottom: 16px; }}
        .footer-banner .btn {{ background: #fff; color: {p['accent']}; padding: 12px 40px; border-radius: 30px; text-decoration: none; font-weight: 700; display: inline-block; }}
        
        footer {{ background: #171c2b; padding: 40px 20px; text-align: center; }}
        footer a {{ color: #ccc; text-decoration: none; margin: 0 12px; font-size: 14px; }}
        footer .copyright {{ color: #666; font-size: 12px; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto; }}
        
        @media (max-width: 768px) {{
            .under-header h1 {{ font-size: 28px; }}
            article h2 {{ font-size: 24px; }}
        }}
    </style>
    <!-- Yandex.Metrika -->
    <script type="text/javascript">
        (function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,'script','https://mc.yandex.ru/metrika/tag.js?id={p['metrika']}','ym');
        ym({p['metrika']}, 'init', {{ssr:true,webvisor:true,clickmap:true,accurateTrackBounce:true,trackLinks:true}});
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/{p['metrika']}" style="position:absolute;left:-9999px" alt=""/></div></noscript>
</head>
<body>
<a href="{p['cta_url']}" target="_blank" class="header-banner">
    <div class="logo">{p['brand']}</div>
    <p>Специальное предложение — бесплатный старт</p>
    <div class="btn">Перейти</div>
</a>
<header>
    <div class="header-wrapper">
        <a href="/" class="logo">{p['brand']}</a>
    </div>
</header>
<main>
    <section class="under-header">
        <div class="date">Обновлено: июль 2026</div>
        <h1>{data["h1"]}</h1>
        <p>{data["subtitle"]}</p>
        <a href="{p['cta_url']}" class="btn">{data["cta_text"]}</a>
    </section>
    
    <div class="container">
        {rating_html}
        
        <article>
            {sections_html}
            {brand_html}
        </article>
    </div>
    
    <section class="faq">
        <h2>Часто спрашивают</h2>
        <div class="accordion">{faq_html}</div>
    </section>
    
    <div class="footer-banner">
        <p>Готовы начать?</p>
        <a href="{p['cta_url']}" class="btn">{data["cta_text"]}</a>
    </div>
</main>
<footer>
    <a href="{p['main_url']}">Основной сайт</a>
    <a href="/about.html">О проекте</a>
    <a href="/faq.html">FAQ</a>
    <div class="copyright">© 2026 {p['brand']}. Информационный партнёр {p['main_url']}. Все права защищены.</div>
</footer>
<script>
document.querySelectorAll('.accordion-header').forEach(h => {{
    h.addEventListener('click', () => {{
        const item = h.parentElement;
        const active = item.classList.contains('active');
        document.querySelectorAll('.accordion-item').forEach(el => el.classList.remove('active'));
        if (!active) item.classList.add('active');
    }});
}});
</script>
</body>
</html>'''
    
    path = Path(f"/root/seo-landings-v2/{p['slug']}.html")
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text(html)
    
    # Count sections
    h2_count = html.count('<h2')
    h3_count = html.count('<h3')
    h4_count = html.count('<h4')
    total_sections = h2_count + h3_count + h4_count
    print(f"  ✓ {path.name}: {len(html):,} bytes, {total_sections} sections (H2:{h2_count} H3:{h3_count} H4:{h4_count})")

print("\n✅ All pages generated in /root/seo-landings-v2/")
