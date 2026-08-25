from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("tactics"))
async def tactics_command(message: types.Message):
    # You can expand this with real data from football-data skill
    tactics_content = (
        "⚽ <b>La Liga Tactical Focus</b>\n\n"
        "This section provides in-depth tactical analysis of La Liga matches.\n\n"
        "📌 <b>Key Topics:</b>\n"
        "• Pressing patterns & high lines\n"
        "• Positional play & attacking structures\n"
        "• Set-piece routines & defensive organization\n"
        "• Managerial strategies & substitutions\n\n"
        "📅 <i>Coming soon: Real-time tactical breakdowns!</i>"
    )
    await message.answer(tactics_content)
