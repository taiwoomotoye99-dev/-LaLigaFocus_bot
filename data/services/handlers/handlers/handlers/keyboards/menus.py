from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import inline_keyboard

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Standings", callback_data="standings"),
            InlineKeyboardButton(text="📅 Fixtures", callback_data="fixtures")
        ],
        [
            InlineKeyboardButton(text="⚽ Tactics", callback_data="tactics"),
            InlineKeyboardButton(text="👤 Players", callback_data="players")
        ],
        [
            InlineKeyboardButton(text="💰 Finances", callback_data="finances")
        ]
    ])
