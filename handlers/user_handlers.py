from copy import deepcopy

from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from database.database import users_db, user_dict_template
from filters.filters import city_filter
from keyboards.date_kb import create_date_keyboard
from lexicon.lexicon_ru import LEXICON
from models.models import Train


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON['/start'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])

@router.message(Command(commands=['pick_up_train']))
async def process_pick_up_train_command(message: Message):
    await message.answer(text=LEXICON['/pick_up_train'])

@router.message(city_filter)
async def process_date_picker_command(message: Message):
    await message.answer(text=LEXICON['date_picker'], reply_markup=create_date_keyboard())