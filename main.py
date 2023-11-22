from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API

import text_messages


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Словарь для хранения информации о фото для каждого пользователя
user_photo_data = {}


async def on_startup(_):
    print('The bot has been successfully launched!')


# Кнопка "Начать!"
ikb_mido_start = InlineKeyboardMarkup(row_width=2)
ib_mido_poit = [InlineKeyboardButton(text='Начать!', callback_data='mido_poit_start')]
ikb_mido_start.add(*ib_mido_poit)


# Обработка кнопки "Начать!"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_start')
async def handle_button(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Успешно!\nВыберите какой вопрос вас интересует:', reply_markup=ikb_selection)


# Выбор информации
ikb_selection = InlineKeyboardMarkup(row_width=2)
ib_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_generalScheduleSheet')]
ib_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_interSessionSchedule')]
ib_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_sessionSchedule')]
ib_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_listOfTeachers')]
ib_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_liquidationOfDebts')]
ib_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_paymentSchedule')]
ikb_selection.add(*ib_generalScheduleSheet)
ikb_selection.add(*ib_interSessionSchedule)
ikb_selection.add(*ib_sessionSchedule)
ikb_selection.add(*ib_listOfTeachers)
ikb_selection.add(*ib_liquidationOfDebts)
ikb_selection.add(*ib_paymentSchedule)


# 1.1 Функция отправки фотографии .jpg с информацие о расписании занятий
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_generalScheduleSheet')
async def handle_button_gss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_1course
    photo_path = "data/schedule.jpg"
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания.")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)


# 1.2 Функция обработки межсессионного расписания
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_interSessionSchedule')
async def handle_button_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)


# 1.3 Функция обработки график сессий
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_sessionSchedule')
async def handle_button_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)


# 1.4 Функция обработки контактов преподавателей
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_listOfTeachers')
async def handle_button_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)


# 1.5 Функция обработки ликвидации долгов
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_liquidationOfDebts')
async def handle_button_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)


# 1.6 Функция обработки графика оплат
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_paymentSchedule')
async def handle_button_1course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_back)

# Вернуться к выбору интересующей информации
ikb_back = InlineKeyboardMarkup(row_width=2)
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back')]
ikb_back.add(*ib_mido_back)


# Возврат в начало
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back')
async def handle_button_back(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, text=text_messages.START_COMMAND, reply_markup=ikb_mido_start)  # Отправляем команду /start


# Обработчик всех текстовых сообщений (удаляет любые сообщения, кроме команды /start)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_messages(message: types.Message):
    if message.text.strip().lower() == "/start":
        await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido_start)
        await message.delete()
    else:
        await message.delete()


# Обработчик всех медиафайлов (фото, стикеры, GIF и т.д.) (удаляет все медиа типы)
@dp.message_handler(content_types=[
    types.ContentType.PHOTO,
    types.ContentType.STICKER,
    types.ContentType.ANIMATION,
    types.ContentType.VIDEO,
    types.ContentType.DOCUMENT,
    types.ContentType.AUDIO,
    types.ContentType.VOICE,
    types.ContentType.POLL,
    types.ContentType.LOCATION,
    types.ContentType.VIDEO_NOTE,
    types.ContentType.VENUE,
    types.ContentType.GAME,
    types.ContentType.INVOICE,
    types.ContentType.SUCCESSFUL_PAYMENT,
])
async def handle_media_messages(message: types.Message):
    await message.delete()


# Команда /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=text_messages.HELP_COMMAND)


# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido_start)
    await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
