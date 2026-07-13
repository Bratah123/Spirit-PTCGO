import os
import importlib.util
import logging
import sys
from typing import Dict, List
from spirit.game.models.card import Card, PokemonCard
from spirit.game.attributes import AttrID, CardType

class ScriptLoader:
    """Dynamically loads card definition scripts from the filesystem."""
    def __init__(self, scripts_dir: str):
        self.scripts_dir = os.path.abspath(scripts_dir)
        self.cards: List[Card] = []
        self.cards_by_guid: Dict[str, Card] = {}
        self.cards_by_key: Dict[str, Card] = {}
        # script filename stem (e.g. "Watchog_79") -> archetype GUID
        self.cards_by_stem: Dict[str, str] = {}

    def load_all(self, force=False):
        """Loads all card scripts once; cached thereafter unless force=True.

        Re-running scripts rebuilds effect registries (ABILITIES_BY_ID etc.)
        and blocks the event loop ~1s, so hot paths must hit the cache.
        """
        if self.cards and not force:
            return self.cards
        self.cards = []
        self.cards_by_guid = {}
        self.cards_by_key = {}
        self.cards_by_stem = {}
        
        logging.info(f"[Scripts] Loading card scripts from {self.scripts_dir}...")
        
        for root, _, files in os.walk(self.scripts_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    self._load_script(file_path)
        
        logging.info(f"[Scripts] Successfully loaded {len(self.cards)} card scripts.")
        return self.cards

    def _load_script(self, file_path: str):
        """Loads a single card script."""
        try:
            # Create a unique module name based on the relative path
            rel_path = os.path.relpath(file_path, self.scripts_dir)
            module_name = "card_script_" + rel_path.replace(os.path.sep, "_").replace(".py", "")
            
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logging.error(f"[Scripts] Could not create spec or loader for {file_path}")
                return

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'card'):
                card_def = module.card
                # Convert the Definition object into a Server Card model
                # This ensures compatibility with existing packet handlers
                archetype = card_def.to_archetype_dict()
                guid = archetype["guid"]
                key = archetype["key"]
                attrs = archetype["attributes"]
                
                c_type = attrs.get(str(AttrID.CARD_TYPE.value), {}).get("value", CardType.UNSET)
                
                display_name = archetype.get("display_name")
                searchable_by = archetype.get("searchable_by", [])
                subtypes = getattr(card_def, "subtypes", [])

                if c_type == CardType.POKEMON:
                    card_obj = PokemonCard(guid, key, attrs, display_name, searchable_by, subtypes)
                else:
                    card_obj = Card(guid, key, attrs, display_name, searchable_by, subtypes)
                
                self.cards.append(card_obj)
                self.cards_by_guid[guid] = card_obj
                self.cards_by_key[key] = card_obj
                self.cards_by_stem[os.path.splitext(os.path.basename(file_path))[0]] = guid
            else:
                logging.warning(f"[Scripts] Script {file_path} does not define a 'card' object.")
                
        except Exception as e:
            logging.error(f"[Scripts] Failed to load script {file_path}: {e}")

# Global loader instance
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__))
loader = ScriptLoader(SCRIPTS_DIR)
