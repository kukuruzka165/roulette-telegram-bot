import time
from aiogram import Bot, Dispatcher, executor, types
from random import randint

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)  # Надо было срочно переходить на аиограм, а я хз, что это значит. Ладно, хай так и будет

print("Я жив!")
print("Спасибо, что запустил(а) меня!")


@dp.message_handler(commands=["start"])
async def start(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Запрошен старт")

    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btnr = types.KeyboardButton("Играть")
    btna = types.KeyboardButton("Автор")
    btnd = types.KeyboardButton("Отказ от ответственности")
    markup1.add(btnd, btna, btnr)

    send_mess = f"<b>Привет, {message.from_user.first_name}! В этом боте ты сможешь крутить рулетку.</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Важно! </b>В данный момент бот находится на стадии разработки. Он может работать неправильно или " \
                "не работать вовсе. Приношу свои извенения! "
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = f"<b>Вот список доступных " \
                f"команд:</b>\n\n<b>/roll</b> - Сыграть в рулетку (Имеет аналог на клавиатуре)\n<b>/disclaimer</b> - " \
                f"Отказ от ответственности (Имеет аналог на клавиатуре)\n<b>/ping</b> - Понг!\n<b>/author</b> - Автор " \
                f"бота (Имеет аналог на клавиатуре)\n\n<b>Или пользуйся клавиатурой с кнопками:</b> "
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Удачи!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    print("Старт успешно отправлен!")


@dp.message_handler(commands=["roll"])
async def roll(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Крутим!")
    rnd = randint(1, 37)
    print("Выпал из 37 вариант", rnd)

    # Старый, нерабочий и тупой говнокод, который я из вредности не выразаю :-) :
    # if rnd == 0:
    #    color = "🟢 Зелёный"
    # else:
    #    if rnd == 32 or 19 or 21 or 25 or 34 or 27 or 36 or 30 or 23 or 5 or 16 or 1 or 14 or 9 or 18 or 7 or 12 or 3:
    #        color = "🔴 Красный"
    # Не бейте за новый говнокод, мне так понятнее просто
    result = "Ошибка!"
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
    send_mess = f"<b>{message.from_user.first_name}, ваш результат:\n{result}</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    print("Прокрутили! Результат -", result)


@dp.message_handler(commands=["ping"])
async def ping(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Пинг?")
    send_mess = f"<b>Понг! Я жив!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    print("Понг!")


@dp.message_handler(commands=["disclaimer"])
async def disclaimer(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Запрошен дисклеймер.")
    send_mess = "<b>ДИСКЛЕЙМЕР (ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ): </b>Я полностью отказываюсь от результатов использования " \
                "данного бота не в целях развлечения. Бот создан не в коммерческих целях, и никогда таким не " \
                "станет!\n\n<b>Коротко:</b> Ставок нет."
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    print("Дисклеймер отправлен.")


@dp.message_handler(commands=["author"])
async def author(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Запрошен автор.")
    send_mess = f"<b>Мой автор - @anton165</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    print("Автор заслан)")


@dp.message_handler(commands=["keyboard"])
async def keyboard(message):
    print("")
    print("--------------------")
    print(time.ctime())
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    print("-")
    print("Запрошено открытие клавиатуры!")
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btnr = types.KeyboardButton("Играть")
    btna = types.KeyboardButton("Автор")
    btnd = types.KeyboardButton("Отказ от ответственности")
    # markup1.add(btnr, btna, btnd)
    markup1.add(btnd, btna, btnr)
    send_mess = f"<b>Клавиатура открыта!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup1)
    print("Клавиатура открыта)")


@dp.message_handler(content_types=["text"])
async def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "играть":
        await roll(message)
    else:
        if get_message_bot == "автор":
            await author(message)
        else:
            if get_message_bot == "отказ от ответственности":
                await disclaimer(message)
            else:
                print("")
                print("--------------------")
                print(time.ctime())
                print(message.from_user.first_name, message.from_user.last_name,
                      "@", message.from_user.username, "id =", message.from_user.id)
                print(message.chat_title)
                print("-")
                print("Прислал(а):", message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
