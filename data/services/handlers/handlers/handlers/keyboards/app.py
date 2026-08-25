import asyncio
import logging
from loader import bot, dp
from handlers import start, standings, fixtures, tactics, players, finances, results

# Register all handlers
dp.include_router(start.router)
dp.include_router(standings.router)
dp.include_router(fixtures.router)
dp.include_router(tactics.router)
dp.include_router(players.router)
dp.include_router(finances.router)
dp.include_router(results.router)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
