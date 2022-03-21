import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


# Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(
        level=level, category=category, subcategory=subcategory, item_id=item_id
    )


# Bizning menu 3 qavat (LEVEL) dan iborat
# 0 - Kategoriyalar
# 1 - Ost-kategoriyalar
# 2 - Mahsulotlar
# 3 - Yagona mahsulot


# Kategoriyalar uchun keyboardyasab olamiz
async def categories_keyboard():
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 0

    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    # Bazadagi barcha kategoriyalarni olamiz
    categories = await db.get_categories()
    # Har bir kategoriya uchun quyidagilarni bajaramiz:
    for category in categories:
        # Kategoriyaga tegishli mahsulotlar sonini topamiz
        number_of_items = await db.count_products(category["category_code"])

        # Tugma matnini yasab olamiz
        button_text = f"{category['category_name']} ({number_of_items} dona)"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, category=category["category_code"]
        )

        # Tugmani keyboardga qo'shamiz
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Keyboardni qaytaramiz
    return markup


# Berilgan kategoriya ostidagi kategoriyalarni qaytaruvchi keyboard
async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    # Kategoriya ostidagi kategoriyalarni bazadan olamiz
    subcategories = await db.get_subcategories(category)
    for subcategory in subcategories:
        # Kategoriyada nechta mahsulot borligini tekshiramiz
        number_of_items = await db.count_products(
            category_code=category, subcategory_code=subcategory["subcategory_code"]
        )

        # Tugma matnini yasaymiz
        button_text = f"{subcategory['subcategory_name']} ({number_of_items} dona)"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory["subcategory_code"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Ortga qaytish tugmasini yasaymiz (yuoqri qavatga qaytamiz)
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


# Ostkategoriyaga tegishli mahsulotlar uchun keyboard yasaymiz
async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2

    markup = InlineKeyboardMarkup(row_width=1)

    # Ost-kategorioyaga tegishli barcha mahsulotlarni olamiz
    items = await db.get_products(category, subcategory)
    for item in items:
        # Tugma matnini yasaymiz
        button_text = f"{item['productname']} - ${item['price']}"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory,
            item_id=item["id"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Ortga qaytish tugmasi
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category
            ),
        )
    )
    return markup


# Berilgan mahsulot uchun Xarid qilish va Ortga yozuvlarini chiqaruvchi tugma keyboard
def item_keyboard(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=f"🛒 Xarid qilish", callback_data=buy_item.new(item_id=item_id)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category, subcategory=subcategory
            ),
        )
    )
    return markup
