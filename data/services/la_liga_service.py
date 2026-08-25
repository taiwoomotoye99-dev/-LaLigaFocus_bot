from sports_skills_football_data import (
    get_current_season,
    get_season_standings,
    get_season_schedule,
    get_event_summary,
    get_daily_schedule
)

class LaLigaService:
    COMPETITION_ID = "la-liga"
    
    @staticmethod
    def get_current_season_id():
        """Get the current La Liga season ID"""
        try:
            season = get_current_season(competition_id=LaLigaService.COMPETITION_ID)
            return season["id"]
        except Exception as e:
            return None
    
    @staticmethod
    def get_standings():
        """Get current La Liga standings"""
        season_id = LaLigaService.get_current_season_id()
        if not season_id:
            return None
        try:
            return get_season_standings(season_id=season_id)
        except Exception:
            return None
    
    @staticmethod
    def get_fixtures():
        """Get upcoming La Liga fixtures"""
        season_id = LaLigaService.get_current_season_id()
        if not season_id:
            return None
        try:
            return get_season_schedule(season_id=season_id)
        except Exception:
            return None
    
    @staticmethod
    def get_daily_matches(date: str = None):
        """Get matches for a specific date"""
        import datetime
        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            return get_daily_schedule(date=date)
        except Exception:
            return None
