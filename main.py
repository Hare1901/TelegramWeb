
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

from config import *

# ссылка на сайт, который откроется ппри нажатии на кнопку открыть сайт
# сайт должен нахоодиться на удаленном сервере(обязательно), можно использовать гитхаб.
website = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу', web_app=WebAppInfo(url=website)))
    await message.answer("Приветствую!", reply_markup=markup)

executor.start_polling(dp)