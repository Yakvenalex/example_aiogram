from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from create_bot import dp, bot, admins, loger
import os
from async_bd import check_referral, add_user_if_not_exists, insert_into_vpn_keys

current_dir = os.path.dirname(os.path.abspath(__file__))



@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.chat.id, 'Я готов к настройке')


@dp.callback_query_handler(text=['back_home'], state='*')
async def back_home(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    await bot.send_message(call.from_user.id, 'Я готов к настройке')



# @dp.message_handler(content_types=[types.ContentType.PHOTO])
# async def photo_handler(message: types.Message):
#     # Получение информации о фото
#     photo = message.photo[-1]  # Берем самую большую версию фото
#     photo_id = photo.file_id
#
#     # Отправка сообщения с ID фото
#     await message.reply(f"ID фото: `{photo_id}`", parse_mode=types.ParseMode.MARKDOWN)
