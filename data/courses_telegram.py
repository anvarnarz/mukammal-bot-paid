from aiogram import types

courses = [
    {
        "id": "001",
        "title": "#01 KURS BILAN TANISHUV",
        "url": "https://youtu.be/oRSa8NXWMXQ",
        "description": "Kurs haqida ma'lumot."
    },
    {
        "id": "002",
        "title": "#02 KERAKLI DASTURLAR",
        "url": "https://youtu.be/5qUTBMJLGfM",
        "description": "Bot yaratish uchun kerakli dasturlarni o'rnatamiz."
    },
    {
        "id": "003",
        "title": "#03 METODOLOGIYA",
        "url": "https://youtu.be/8nsEBxH7IYA",
        "description": "Dasturlash metodologiyasi bilan tanishamiz"
    }
]

inline_results_telegram = []
for course in courses:
    inline_results_telegram.append(types.InlineQueryResultArticle(
        id=course["id"],
        title=course["title"],
        input_message_content=types.InputTextMessageContent(
            message_text=f"{course['title']} darsiga link: {course['url']}",
            parse_mode="HTML"
        ),
        url=course['url'],
        description=course['description']
    ))
