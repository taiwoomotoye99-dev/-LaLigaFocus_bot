from aiogram import Router, types
from aiogram.filters import Command
from services.la_liga_service import LaLigaService

router = Router()

@router.message(Command("standings"))
async def standings_command(message: types.Message):
    await message.answer("📊 Fetching La Liga standings...")
    
    standings_data = LaLigaService.get_standings()
    
    if not standings_data:
        await message.answer("⚠️ Could not fetch standings. Please try again later.")
        return
    
    # Format standings into readable text
    response = "🏆 <b>La Liga Standings</b>\n\n"
    for i, team in enumerate(standings_data[:10], 1):
        response += f"{i}. {team['name']} — {team['points']} pts\n"
    
    await message.answer(response)
