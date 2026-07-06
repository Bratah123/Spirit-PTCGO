import os
import json
import logging
import time
from typing import List, Optional
from spirit.game.models.versus import VersusSeason

SEASONS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'database', 'json_data', 'versus_seasons.json'
))

class VersusSeasonManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VersusSeasonManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.seasons: List[VersusSeason] = []
        self.load_seasons()

    def load_seasons(self):
        path = SEASONS_PATH
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                self.seasons = [VersusSeason.from_dict(s) for s in data]
                logging.info(f"[SeasonManager] Loaded {len(self.seasons)} versus seasons from {path}")
            except Exception as e:
                logging.error(f"[SeasonManager] Failed to load versus seasons: {e}")
                self.seasons = []
        else:
            logging.warning(f"[SeasonManager] versus_seasons.json not found at {path}")
            self.seasons = []

    def get_active_season(self) -> Optional[VersusSeason]:
        """Returns the currently active VersusSeason based on current timestamp, or the first one as default."""
        current_time_ms = int(time.time() * 1000)
        for season in self.seasons:
            if season.start_time <= current_time_ms <= season.end_time:
                return season
        # Fallback to the first season if none active
        if self.seasons:
            return self.seasons[0]
        return None
