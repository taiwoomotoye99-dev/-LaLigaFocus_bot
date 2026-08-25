from aiogram import Router, types
from aiogram.filters import Command
from keyboards.menus import main_menu

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "⚽ <b>La Liga Focus Bot</b>\n\n"
        "Your companion for tactical breakdowns, player profiles, "
        "and club finances from Spain's top football league.\n\n"
        "📋 <b>Commands:</b>\n"
        "/tactics - Tactical analysis\n"
        "/players - Player profiles\n"
        "/finances - Club finance insights\n"
        "/standings - Current La Liga table\n"
        "/fixtures - Upcoming matches\n"
        "/results - Recent match results\n"
        "/help - Show this menu",
        reply_markup=main_menu()
    )
