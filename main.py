import asyncio
from random import choice
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

HEART = '🤍'
COLORED_HEARTS = ['💗', '💓', '💖', '💘', '❤️', '💞']
MAGIC_PHRASES = ['magic']
EDIT_DELAY = 0.10

PARADE_MAP = '''
00000000000
00111011100
01111111110
01111111110
00111111100
00011111000
00001110000
00000100000
'''


def generate_parade_colored():
    output = ''
    for c in PARADE_MAP:
        if c == '0':
            output += HEART
        elif c == '1':
            output += choice(COLORED_HEARTS)
        else:
            output += c
    return output


@dp.message_handler(commands=['start'])
async def animation_handler(message: Message):
    await message.answer("""Поздравляю с 8 Марта\nИ желаю я тепла,\nМного радости, подарков,\nЛюбви, счастья и добра!""")
    upload_message = await bot.send_message(chat_id=message.chat.id, text="ОЖИДАЙТЕ!!!")
    await asyncio.sleep(1)
    with open("animation.gif", "rb") as f:
        await message.answer_video(f)
    for i in range(50):
        text = generate_parade_colored()
        await upload_message.edit_text(text)
        await asyncio.sleep(EDIT_DELAY)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
