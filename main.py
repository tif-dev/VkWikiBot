# Импорт модулей
import wikipedia
from vkbottle.bot import Bot, Message

# Импорт конфига
import config

bot = Bot(config.TOKEN)  # В файле config.py нужно указать токен Вашей группы

wikipedia.set_lang("RU")  # Язык википедии


@bot.on.message(text=['/wiki <item>', '/wiki'])
async def any_message(message: Message, item=None):
    if item is not None:
        await message.answer("Так-с, кажется я что-то нашел:\n\n" + wikipedia.summary(item))
    else:
        await message.answer("Ошибка. Введите запрос.", attachment='doc395332977_545973204')


bot.run_forever()
