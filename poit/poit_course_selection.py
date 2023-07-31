from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API

from .poit_1st_course import ikb_poit_1st_course
from .poit_2nd_course import ikb_poit_2nd_course
from .poit_3rd_course import ikb_poit_3rd_course
from .poit_4th_course import ikb_poit_4th_course
from .poit_5th_course import ikb_poit_5th_course


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

#Выбор курса ПОИТ
ikb_poit_course_selection = InlineKeyboardMarkup(row_width=2)
ib_poit_1st_course = [InlineKeyboardButton(text='1 курс', callback_data='poit_1st_course')]
ib_poit_2nd_course = [InlineKeyboardButton(text='2 курс', callback_data='poit_2nd_course')]
ib_poit_3rd_course = [InlineKeyboardButton(text='3 курс', callback_data='poit_3rd_course')]
ib_poit_4th_course = [InlineKeyboardButton(text='4 курс', callback_data='poit_4th_course')]
ib_poit_5th_course = [InlineKeyboardButton(text='5 курс', callback_data='poit_5th_course')]
ib_back_beginning = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_course_selection.add(*ib_poit_1st_course)
ikb_poit_course_selection.add(*ib_poit_2nd_course)
ikb_poit_course_selection.add(*ib_poit_3rd_course)
ikb_poit_course_selection.add(*ib_poit_4th_course)
ikb_poit_course_selection.add(*ib_poit_5th_course)
ikb_poit_course_selection.add(*ib_back_beginning)


#1 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1st_course')
async def handle_button_1course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1 курс ПОИТ!\nВыберите, что Вас интересует:',
                           reply_markup=ikb_poit_1st_course)


#2 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2nd_course')
async def handle_button_2course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:',
                           reply_markup=ikb_poit_2nd_course)


#3 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3rd_course')
async def handle_button_3course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 3 курс ПОИТ!\nВыберите, что Вас интересует:',
                           reply_markup=ikb_poit_3rd_course)


#4 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4th_course')
async def handle_button_4course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 4 курс ПОИТ!\nВыберите, что Вас интересует:',
                           reply_markup=ikb_poit_4th_course)


#5 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5th_course')
async def handle_button_5course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 5 курс ПОИТ!\nВыберите, что Вас интересует:',
                           reply_markup=ikb_poit_5th_course)
