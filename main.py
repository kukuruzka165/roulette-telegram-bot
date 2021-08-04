from config import TOKEN  # , gif_id
import time
from aiogram import Bot, Dispatcher, executor, types
from random import randint
import asyncio
import requests


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print("Я жив!")
print("Спасибо, что запустил(а) меня!")


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

    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btnr = types.KeyboardButton("Играть")
    btna = types.KeyboardButton("Автор")
    btnd = types.KeyboardButton("Случайный факт")
    markup1.add(btnd, btna, btnr)

    send_mess = f"<b>Привет, {message.from_user.first_name}! В этом боте ты сможешь крутить рулетку.</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Поскольку бот бесплатный, он не хостится на удалённом сервере. Из-за этого я не могу держать его включённым 24/7. Приношу свои извинения!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Важно для владельцев групп: </b>\nУ бота ограничен доступ к сообщениям в группах на уровне Telegram API. Он не сможет за вами подглядывать :)\n<b><a href='https://core.telegram.org/bots#privacy-mode'>Подробнее</a></b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)

    send_mess = "<b>Вот список доступных команд:</b>\n\n<b>/roll</b> - Играть в рулетку (Имеет аналог на клавиатуре)\n\n<b>/orlanka</b> - Играть в орлянку (орёл или решка)\n\n<b>/dice</b> - Подбросить кости\n\n<b>/fact</b> - Случаный факт про этого бота (Имеет аналог на клавиатуре)\n\n<b>/disclaimer</b> - Отказ от ответственности\n\n<b>/author</b> - Автор бота (Имеет аналог на клавиатуре)\n\n<b>/ping</b> - Понг!\n\n<b>/keyboard</b> - Открыть заново клавиатуру для игры. Полезно в группах\n\n\n<b>Или пользуйся клавиатурой с кнопками:</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Удачи!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup1)

    await log("Старт отправлен!")


@dp.message_handler(commands=["roll"])
async def roll(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    gamecode = randint(1000, 9999)
    await log(f"{gamecode} - Запрошено кручение!")
    send_mess = "<b>Ожидание ответа от random.org</b>"
    roll_mess = await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)
    roll_mess_id = roll_mess.message_id

    #  rnd_sleep = randint(1, 3)
    #  rnd = randint(1, 37)
    rnd = randomorg_parse(37)
    await log(f"{gamecode} - Выпал вариант {rnd} из 37.")

    #  elif? Нет, не учили)

    result = "Ошибка. Вероятнее всего проблема на стороне random.org"
    if rnd == 1:
        result = "Зеро! 🟢 Зелёный"
    else:
        if rnd == 2:
            result = "32, 🔴 Красный"
        else:
            if rnd == 3:
                result = "15, ⚫ Чёрный"
            else:
                if rnd == 4:
                    result = "19, 🔴 Красный"
                else:
                    if rnd == 5:
                        result = "4, ⚫ Чёрный"
                    else:
                        if rnd == 6:
                            result = "21, 🔴 Красный"
                        else:
                            if rnd == 7:
                                result = "2, ⚫ Чёрный"
                            else:
                                if rnd == 8:
                                    result = "25, 🔴 Красный"
                                else:
                                    if rnd == 9:
                                        result = "17, ⚫ Чёрный"
                                    else:
                                        if rnd == 10:
                                            result = "34, 🔴 Красный"
                                        else:
                                            if rnd == 11:
                                                result = "6, ⚫ Чёрный"
                                            else:
                                                if rnd == 12:
                                                    result = "27, 🔴 Красный"
                                                else:
                                                    if rnd == 13:
                                                        result = "13, ⚫ Чёрный"
                                                    else:
                                                        if rnd == 14:
                                                            result = "36, 🔴 Красный"
                                                        else:
                                                            if rnd == 15:
                                                                result = "11, ⚫ Чёрный"
                                                            else:
                                                                if rnd == 16:
                                                                    result = "30, 🔴 Красный"
                                                                else:
                                                                    if rnd == 17:
                                                                        result = "8, ⚫ Чёрный"
                                                                    else:
                                                                        if rnd == 18:
                                                                            result = "23, 🔴 Красный"
                                                                        else:
                                                                            if rnd == 19:
                                                                                result = "10, ⚫ Чёрный"
                                                                            else:
                                                                                if rnd == 20:
                                                                                    result = "5, 🔴 Красный"
                                                                                else:
                                                                                    if rnd == 21:
                                                                                        result = "24, ⚫ Чёрный"
                                                                                    else:
                                                                                        if rnd == 22:
                                                                                            result = "16, 🔴 Красный"
                                                                                        else:
                                                                                            if rnd == 23:
                                                                                                result = "33, ⚫ Чёрный"
                                                                                            else:
                                                                                                if rnd == 24:
                                                                                                    result = "1, 🔴 Красный"
                                                                                                else:
                                                                                                    if rnd == 25:
                                                                                                        result = "20, ⚫ Чёрный"
                                                                                                    else:
                                                                                                        if rnd == 26:
                                                                                                            result = "14, 🔴 Красный"
                                                                                                        else:
                                                                                                            if rnd == 27:
                                                                                                                result = "31, ⚫ Чёрный"
                                                                                                            else:
                                                                                                                if rnd == 28:
                                                                                                                    result = "9, 🔴 Красный"
                                                                                                                else:
                                                                                                                    if rnd == 29:
                                                                                                                        result = "22, ⚫ Чёрный"
                                                                                                                    else:
                                                                                                                        if rnd == 30:
                                                                                                                            result = "18, 🔴 Красный"
                                                                                                                        else:
                                                                                                                            if rnd == 31:
                                                                                                                                result = "29, ⚫ Чёрный"
                                                                                                                            else:
                                                                                                                                if rnd == 32:
                                                                                                                                    result = "7, 🔴 Красный"
                                                                                                                                else:
                                                                                                                                    if rnd == 33:
                                                                                                                                        result = "28, ⚫ Чёрный"
                                                                                                                                    else:
                                                                                                                                        if rnd == 34:
                                                                                                                                            result = "12, 🔴 Красный"
                                                                                                                                        else:
                                                                                                                                            if rnd == 35:
                                                                                                                                                result = "35, ⚫ Чёрный"
                                                                                                                                            else:
                                                                                                                                                if rnd == 36:
                                                                                                                                                    result = "3, 🔴 Красный"
                                                                                                                                                else:
                                                                                                                                                    if rnd == 37:
                                                                                                                                                        result = "26, ⚫ Чёрный"

    await log(f"{gamecode} - Результат - {result}.")  # Ждём {rnd_sleep} сек...")
    #  await asyncio.sleep(rnd_sleep)

    await bot.edit_message_text(chat_id=message.chat.id, message_id=roll_mess_id, text=f"<b>{message.from_user.first_name}, ваш результат:\n{result}</b>", parse_mode="html", disable_web_page_preview=True)
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
    send_mess = f"<b>🧑🏻‍💻 Мой автор - @anton165</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Автор заслан)")


@dp.message_handler(commands=["keyboard"])
async def keyboard(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошено открытие клавиатуры!")
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btnr = types.KeyboardButton("Играть")
    btna = types.KeyboardButton("Автор")
    btnd = types.KeyboardButton("Случайный факт")
    # markup1.add(btnr, btna, btnd)
    markup1.add(btnd, btna, btnr)
    send_mess = f"<b>Клавиатура открыта!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup1)
    await log("Клавиатура открыта)")


@dp.message_handler(commands=["orlanka"])
async def orlanka(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("У меня попросили орла и решку. Делаю.")
    send_mess = f"<b>Ожидание ответа от random.org</b>"
    oreshka_mess = await bot.send_message(message.chat.id, send_mess, parse_mode="html", disable_web_page_preview=True)
    oreshka_mess_id = oreshka_mess.message_id
    #  oreshka = randint(1, 2)
    oreshka = randomorg_parse(2)

    #  elif? Нет, не учили)

    resultoreshka = "Ошибка. Вероятнее всего проблема на стороне random.org"
    if oreshka == 1:
        await log("Выпал орёл. Засылаю..")
        resultoreshka = "Орёл"
    else:
        if oreshka == 2:
            await log("Выпала решка. Засылаю..")
            resultoreshka = "Решка"

    await bot.edit_message_text(chat_id=message.chat.id, message_id=oreshka_mess_id, text=f"<b>{message.from_user.first_name}, ваш результат:\n{resultoreshka}.</b>", parse_mode="html")
    await log("Отправлено.")


@dp.message_handler(commands=["dice"])
async def dice(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    gamecode = randint(100, 999)
    dice_sleep = 3
    await log(f"{gamecode} - Запрошен дайс.")
    dice_message = await bot.send_dice(message.chat.id, emoji="🎲")
    await log(f"{gamecode} - Подкинул. Результат: {dice_message.dice.value}. Ждём {dice_sleep} сек...")
    send_mess = f"<b>Пожалйста подождите..</b>"
    dice_comment_message = await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    #  elif? Нет, не учили)

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

    #  elif? Нет, не учили)

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


if __name__ == '__main__':
    executor.start_polling(dp)
