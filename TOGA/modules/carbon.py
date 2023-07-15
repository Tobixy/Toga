from pyrogram.types import Message
from pyrogram import filters
from TOGA import pgram
from TOGA.utils.errors import capture_err
from io import BytesIO
import requests


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    response = requests.post(url, json={"code": code})
    image = BytesIO(response.content)
    image.name = "carbon.png"
    return image


@pgram.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a text to generate Carbon.")
    if not message.reply_to_message.text:
        return await message.reply_text("Reply to a text to generate Carbon.")
    m = await message.reply_text("Generating Carbon...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading Generated Carbon...")
    await pgram.send_photo(message.chat.id, photo=carbon)
    await m.delete()
    carbon.close()


__mod_name__ = "Carbon"
