from aiogram import types

courses = [
    {
        "id": "001",
        "title": "#01 KERAKLI DASTURLAR",
        "url": "https://python.sariq.dev/ilk-qadamlar/01-software",
        "description": "Ushbu bo'limda Python tilida kod yozish uchun kerak bo'lgan dasturlarni o'rnatamiz"
    },
    {
        "id": "002",
        "title": "#02 HELLO WORLD!",
        "url": "https://python.sariq.dev/ilk-qadamlar/hello-world",
        "description": "Pythonda birinchi dasturimizni yozamiz."
    },
    {
        "id": "003",
        "title": "#03 PRINT(), SINTEKS VA ARIFMETIK AMALLAR",
        "url": "https://python.sariq.dev/ilk-qadamlar/03-print",
        "description": "print() funktsiyasi, Python sintaksi va arifmetik amallar"
    }
]

inline_results_python = []
for course in courses:
    inline_results_python.append(types.InlineQueryResultArticle(
        id=course["id"],
        title=course["title"],
        input_message_content=types.InputTextMessageContent(
            message_text=f"{course['title']} darsiga link: {course['url']}",
            parse_mode="HTML"
        ),
        url=course['url'],
        description=course['description']
    ))
