import asyncio
from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from motor.motor_asyncio import AsyncIOMotorClient
from app import ft, main as flet_main

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Click', web_app=WebAppInfo(url='http://localhost:8000')
    )
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Click!', reply_markup=webapp_builder())

async def main_bot() -> None:
    bot = Bot('7043516303:AAHKrqjGZ7ki5fgMd7MKRaDpgwhY1PZ1X-U')
    cluster = AsyncIOMotorClient(host='localhost', port=8000)
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

async def run_bot():
    await main_bot()

if __name__ == '__main__':
    asyncio.run(run_bot())