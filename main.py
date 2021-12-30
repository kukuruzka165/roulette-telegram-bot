import time
from random import randint
import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import requests
from algorithm import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markup1.add(types.KeyboardButton("Случайный факт"), types.KeyboardButton("Автор"), types.KeyboardButton("Играть"))
helpmsg = "<b>Вот список доступных команд:</b>\n\n<b>/roll</b> - Играть в рулетку (Также есть на клавиатуре)\n\n<b>/orlanka</b> - Играть в орлянку (орёл или решка)\n\n<b>/dice</b> - Подбросить кости\n\n<b>/fact</b> - Случаный факт про этого бота (Также есть на клавиатуре)\n\n<b>/disclaimer</b> - Отказ от ответственности\n\n<b>/author</b> - Автор бота (Также есть на клавиатуре)\n\n<b>/ping</b> - Понг!\n\n<b>/keyboard</b> - Открыть заново клавиатуру для игры\n\n<b>/rm_keyboard</b> - Закрыть клавиатуру. Полезно в группах\n\n<b>/help</b> - Показать все команды"

print(r"   ____                   ____              __     __  __            ____        __ ")
print(r"  / __ \____  ___  ____  / __ \____  __  __/ /__  / /_/ /____       / __ )____  / /_")
print(r" / / / / __ \/ _ \/ __ \/ /_/ / __ \/ / / / / _ \/ __/ __/ _ \     / __  / __ \/ __/")
print(r"/ /_/ / /_/ /  __/ / / / _, _/ /_/ / /_/ / /  __/ /_/ /_/  __/    / /_/ / /_/ / /_  ")
print(r"\____/ .___/\___/_/ /_/_/ |_|\____/\__,_/_/\___/\__/\__/\___/    /_____/\____/\__/   by @anton165")
print(r"    /_/                                                                             ")


async def log(text):
    print(text)
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n{text}")


def randomorg_parse(number):
    site = requests.get(f'https://www.random.org/integers/?num=1&min=1&max={number}&col=1&base=10&format=plain&rnd=new')
    randomorg_string = int("".join(c for c in site.text if c.isdecimal()))
    return randomorg_string


@dp.message_handler(commands=["start"])
async def start(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошен старт")

    send_mess = f"<b>Привет, {message.from_user.first_name}! В этом боте ты сможешь крутить рулетку.</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Поскольку бот бесплатный, он не хостится на удалённом сервере. Из-за этого я не могу держать его включённым 24/7. Приношу свои извинения!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Важно для владельцев групп: </b>\nУ бота ограничен доступ к сообщениям в группах на уровне Telegram API. Он не сможет за вами подглядывать :)\n<b><a href='https://core.telegram.org/bots#privacy-mode'>Подробнее</a></b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)

    send_mess = helpmsg + "\n\n\n<b>Или пользуйся клавиатурой с кнопками:</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Удачи!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup1)

    await log("Старт отправлен!")


@dp.message_handler(commands=["roll"])
async def roll(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    send_mess = "<b>Ожидание ответа от random.org</b>"
    roll_mess = await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)
    gamecode = randint(100, 999)
    await log(f"{gamecode} - Обращение к random.org...")

    rnd = randomorg_parse(37)
    result = fun_result(rnd)
    await log(f"{gamecode} - Результат - {result}.")
    await bot.edit_message_text(chat_id=message.chat.id, message_id=roll_mess.message_id, text=f"<b>{message.from_user.first_name}, ваш результат:\n{result}</b>", parse_mode="html", disable_web_page_preview=True)
    await log(f"{gamecode} - Готово.")


@dp.message_handler(commands=["ping"])
async def ping(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Пинг?")
    send_mess = f"<b>Понг! Я жив!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Понг!")


@dp.message_handler(commands=["disclaimer"])
async def disclaimer(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошен дисклеймер.")
    send_mess = "<b>ДИСКЛЕЙМЕР (ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ): </b>Я полностью отказываюсь от результатов использования " \
                "данного бота не в целях развлечения. Бот создан не в коммерческих целях, и никогда таким не " \
                "станет!\n\n<b>Коротко:</b> Ставок нет."
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Дисклеймер отправлен.")


@dp.message_handler(commands=["author"])
async def author(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошен автор.")
    send_mess = f"<b>🧑🏻‍💻 Мой автор - @anton165\nЕму можно давать идеи для новых функций в боте.</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Автор заслан)")


@dp.message_handler(commands=["keyboard"])
async def keyboard(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошено открытие клавиатуры!")
    send_mess = f"<b>Клавиатура открыта!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup1)
    await log("Клавиатура открыта.")


@dp.message_handler(commands=['rm_keyboard'])
async def rm_keyboard(message):
    await log("Запрошено закрытие клавиатуры!")
    send_mess = f"<b>Клавиатура закрыта!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=types.ReplyKeyboardRemove())
    await log("Клавиатура закрыта.")


@dp.message_handler(commands=["orlanka"])
async def orlanka(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    gamecode = randint(10, 99)
    send_mess = "<b>Ожидание ответа от random.org</b>"
    oreshka_mess = await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)
    await log(f"{gamecode} - Запрошена орлянка.")
    oreshka = randomorg_parse(2)

    resultoreshka = "Ошибка. Вероятнее всего проблема на стороне random.org"
    if oreshka == 1:
        await log(f"{gamecode} - Выпал орёл. Отправляю...")
        resultoreshka = "Орёл"
    else:
        if oreshka == 2:
            await log(f"{gamecode} - Выпала решка. Отправляю...")
            resultoreshka = "Решка"

    await bot.edit_message_text(chat_id=message.chat.id, message_id=oreshka_mess.message_id, text=f"<b>{message.from_user.first_name}, ваш результат:\n{resultoreshka}.</b>", parse_mode="html")
    await log("Отправлено.")


@dp.message_handler(commands=["dice"])
async def dice(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    gamecode = randint(10, 99)
    dice_sleep = 3
    await log(f"{gamecode} - Запрошен дайс.")
    dice_message = await bot.send_dice(message.chat.id, emoji="🎲")
    await log(f"{gamecode} - Подкинул. Результат: {dice_message.dice.value}. Ждём {dice_sleep} сек...")
    send_mess = f"<b>Пожалйста подождите..</b>"
    dice_comment_message = await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    dice_emoji = ""
    if dice_message.dice.value == 1:
        dice_emoji = "⚀"
    else:
        if dice_message.dice.value == 2:
            dice_emoji = "⚁"
        else:
            if dice_message.dice.value == 3:
                dice_emoji = "⚂"
            else:
                if dice_message.dice.value == 4:
                    dice_emoji = "⚃"
                else:
                    if dice_message.dice.value == 5:
                        dice_emoji = "⚄"
                    else:
                        if dice_message.dice.value == 6:
                            dice_emoji = "⚅"

    await asyncio.sleep(dice_sleep)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=dice_comment_message.message_id, text=f"<b>{message.from_user.first_name}, ваш результат:\n{dice_emoji} {dice_message.dice.value}</b>", parse_mode="html")
    await log(f"{gamecode} - Готово.")


@dp.message_handler(commands=["fact"])
async def fact(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошен факт.")
    howmanyfacts = 5
    send_fact_mess = "Произошла ошибка!"
    rnd_fact = randint(1, howmanyfacts)

    if rnd_fact == 1:
        send_fact_mess = f"Данный бот является FOSS проектом. Это означает, что его <a href='github.com/KUKURUZKA165/roulette-telegram-bot'>исходный код</a> открыт всем желающим. Любой может проверить честность его работы :)"
    else:
        if rnd_fact == 2:
            send_fact_mess = f"Случайность в данном боте реализована через атмосферный шум (random.org). Соременные технологии не способны предугадать результат вашей игры."
        else:
            if rnd_fact == 3:
                send_fact_mess = f"Бот знает только {howmanyfacts} фактов о себе. Он просто перебирает факты случайным образом и отправяет вам."
            else:
                if rnd_fact == 4:
                    send_fact_mess = f"Этот факт ещё не придумали."
                else:
                    if rnd_fact == 5:
                        send_fact_mess = f"Даже если бы все казино использовали такой же способ получения случайных чисел, как у нас, они бы всё равно вероятнее всего оставались в плюсе."

    await bot.send_message(message.chat.id, "<b>Интересный факт:</b>\n" + send_fact_mess, parse_mode="html", disable_web_page_preview=True)

    await log(f"Я отправил факт {rnd_fact} из {howmanyfacts}. Его содержание:\n{send_fact_mess}")


@dp.message_handler(commands=["help"])
async def help_command(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошена помощь")
    send_mess = helpmsg
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Готово")


@dp.message_handler(content_types=["text"])
async def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "играть":
        await roll(message)
    else:
        if get_message_bot == "автор":
            await author(message)
        else:
            if get_message_bot == "случайный факт":
                await fact(message)
            else:
                await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-\nПрислал(а): {message.text}")
                if message.from_user.id == message.chat.id:
                    send_mess = f"<b>Я вас не понял :(</b>"
                    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
                    await log("Отправил пользователю, что я его не понял")


print(f"Добро пожаловать!")

if __name__ == '__main__':
    executor.start_polling(dp)
