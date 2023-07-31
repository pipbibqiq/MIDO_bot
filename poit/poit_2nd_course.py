from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API
from text_messages import NO_DATA


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


ikb_poit_2nd_course = InlineKeyboardMarkup(row_width=2)
ib_poit_2nd_course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_2nd_course_gss')]
ib_poit_2nd_course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_2nd_course_ss')]
ib_poit_2nd_course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_2nd_course_iss')]
ib_poit_2nd_course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_2nd_course_lot')]
ib_poit_2nd_course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_2nd_course_lod')]
ib_poit_2nd_course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_2nd_course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_2nd_course.add(*ib_poit_2nd_course_generalScheduleSheet)
ikb_poit_2nd_course.add(*ib_poit_2nd_course_sessionSchedule)
ikb_poit_2nd_course.add(*ib_poit_2nd_course_interSessionSchedule)
ikb_poit_2nd_course.add(*ib_poit_2nd_course_listOfTeachers)
ikb_poit_2nd_course.add(*ib_poit_2nd_course_liquidationOfDebts)
ikb_poit_2nd_course.add(*ib_poit_2nd_course_paymentSchedule)
ikb_poit_2nd_course.add(*ib_mido_back)


#Вернуться из любого действия в ПОИТ - 2 курс
ikb_poit_2nd_course_back = InlineKeyboardMarkup(row_width=2)
ib_mido_poit_1course_schedule_backOne = [InlineKeyboardButton(text='Вернуться на один шаг назад', callback_data='mido_poit_2nd_course_backOne')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back2')]
ikb_poit_2nd_course_back.add(*ib_mido_poit_1course_schedule_backOne)
ikb_poit_2nd_course_back.add(*ib_mido_back)


#2.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 2 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_gss')
async def handle_button_2nd_course_gss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    photo_path = "poit_data/poit_2nd_course_schedule.jpg"
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 2 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#2.2 Функция обработки график сессий 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_ss')
async def handle_button_2nd_course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 2 курс ПОИТ.\n' + NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#2.3 Функция обработки межсессионного расписания 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_iss')
async def handle_button_2nd_course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 2 курс ПОИТ.\n' + NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#2.4 Функция обработки контактов преподавателей 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_lot')
async def handle_button_2nd_course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 2 курс ПОИТ.\n' + NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#2.5 Функция обработки ликвидации долгов 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_lod')
async def handle_button_2nd_course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 2 курс ПОИТ.\n' + NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#2.6 Функция обработки графика оплат 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course_ps')
async def handle_button_2nd_course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 2 курс ПОИТ.\n' + NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_poit_2nd_course_back)


#Функция выхода из всех предложенных действий в ПОИТ - 2 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_2nd_course_backOne')
async def handle_button_2nd_course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=ikb_poit_2nd_course)
