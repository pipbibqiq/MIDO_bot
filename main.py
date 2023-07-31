from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API
from poit.poit_course_selection import ikb_poit_course_selection

import text_messages


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Словарь для хранения информации о фото для каждого пользователя
user_photo_data = {}


async def on_startup(_):
    print('The bot has been successfully launched!')


#Выбор специальности МИДО
ikb_mido = InlineKeyboardMarkup(row_width=2)
ib_mido_poit = [InlineKeyboardButton(text='ПОИТ', callback_data='mido_poit')]
ikb_mido.add(*ib_mido_poit)


#Выбор ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit')
async def handle_button(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали ПОИТ!\nВыберите какой у вас курс:', reply_markup=ikb_poit_course_selection)


# Обработчик всех текстовых сообщений (удаляет любые сообщения, кроме команды /start)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_messages(message: types.Message):
    if message.text.strip().lower() == "/start":
        await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido)
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


#Команда /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=text_messages.HELP_COMMAND)


#Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido)
    await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
