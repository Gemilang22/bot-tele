import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Load token dari .env
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

# Cek apakah token berhasil dimuat
if not API_TOKEN:
    raise ValueError("❌ BOT_TOKEN tidak ditemukan. Pastikan ada di file .env")

# Inisialisasi bot dan dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Handler saat /start
@dp.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer(f"Halo, {hbold(message.from_user.full_name)}! 👋\nSaya siap membantu!")

# Handler untuk semua pesan teks
@dp.message()
async def handle_message(message: Message):
    await message.answer(f"Kamu mengirim: {message.text}")

# Fungsi utama untuk menjalankan bot
async def main():
    print("🤖 Bot sedang berjalan...")
    await dp.start_polling(bot)

# Jalankan
if __name__ == "__main__":
    asyncio.run(main())
