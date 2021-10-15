import asyncio

from utils.db_api.db_commands import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz...")
    await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("anvar", "sariqdev", 123456789)
    await db.add_user("olim", "olim223", 12341123)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("John", "JohnDoe", 4388229)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

    #### Mahsulotlar uchun test
    print("Products jadvalini yaratamiz...")
    await db.drop_products()
    await db.create_table_products()
    await db.add_product(
        "food",
        "🍒 Oziq-ovqat",
        "tea",
        "🍵 Choy",
        "Ahmad Tea. Earl Grey",
        "https://ahmadtea.my/wp-content/uploads/2020/08/AHMA-BlackTeas-Earl-Grey-100tb-GT.png",
        10,
        "Ahmad choy",
    )
    await db.add_product(
        "food",
        "🍒 Oziq-ovqat",
        "tea",
        "🍵 Choy",
        "Ahmad Tea. English Brekafast",
        "https://dibaonline.de/media/image/product/196/lg/ahmad-tea-english-breakfast-500g-loose-leaf-tea.png",
        20,
    )
    await db.add_product(
        "food",
        "🍒 Oziq-ovqat",
        "coffee",
        "☕ Kofe",
        "Nescafe Gold",
        "https://www.nescafe.com/mt/sites/default/files/2020-07/nescafe-gold-blend-jar-front-pitch.png",
        15,
        "Discover our signature smooth, rich instant coffee. Coffee connoisseurs will appreciate the well-rounded taste and rich aroma in every cup. Our expertly crafted blend is great for all coffee drinking occasions, whenever you want to make a moment special. So why not relax, enjoy the now and savour the distinctive taste of this premium blend.",
    )
    await db.add_product(
        "food",
        "🍒 Oziq-ovqat",
        "milk",
        "🥛 Sut",
        "Nestle Sut. 1L",
        "https://100comments.com/wp-content/uploads/2017/03/nestle-just-milk-low-fat.jpg",
        2,
    )
    await db.add_product(
        "electronics",
        "🖥️ Elektronika",
        "phone",
        "📱 Telefonlar",
        "iPhone 13",
        "https://9to5mac.com/wp-content/uploads/sites/6/2021/09/iphone-13-pro-max-tidbits-9to5mac.jpg",
        1000,
        "Yangi iPhone 13",
    )
    await db.add_product(
        "electronics",
        "🖥️ Elektronika",
        "laptop",
        "💻 Noutbuklar",
        "macBook Air",
        "https://checheelectronics.co.ke/wp-content/uploads/2021/06/NL244a1b_2.jpg",
        1600,
    )

    categories = await db.get_categories()
    print(f"{categories=}")
    print(categories[0]["category_code"])

    subcategories = await db.get_subcategories("food")
    print(f"{subcategories=}")
    print(subcategories[0]["subcategory_name"])

    count_products = await db.count_products("food")
    print(f"{count_products=}")

    count_sub_products = await db.count_products("food", "tea")
    print(f"{count_sub_products=}")

    products = await db.get_products("food", "tea")
    print(f"{products=}")

    product = await db.get_product(1)
    print(f"{product=}")
    product = await db.get_product(5)
    print(f"{product=}")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
