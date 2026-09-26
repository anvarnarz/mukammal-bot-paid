from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
#     New version
# =================================================
# aiogram version 2.18

    form = aiohttp.FormData(quote_fields=False)
    downloaded_photo = await photo.download(destination_file=BytesIO())
    form.add_field(
        name="file",
        value=downloaded_photo
    )

    session = await bot.get_session()
    response = await session.post(url="https://telegra.ph/upload", data=form)
    json_response = await response.json()

    link = 'http://telegra.ph/' + json_response[0]["src"]
    return link



    
#     Old version
# =================================================
#     with await photo.download(BytesIO()) as file:
#         form = aiohttp.FormData()
#         form.add_field(
#             name='file',
#             value=file,
#         )
#         async with bot.session.post('https://telegra.ph/upload', data=form) as response:
#             img_src = await response.json()

#     link = 'http://telegra.ph/' + img_src[0]["src"]
#     return link
