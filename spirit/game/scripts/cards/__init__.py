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
        self.definitions = {}
        self.last_errors = []

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
        self.definitions = {}
        self.last_errors = []
        
        logging.info(f"[Scripts] Loading card scripts from {self.scripts_dir}...")
        
        for root, dirs, files in os.walk(self.scripts_dir):
            dirs.sort()
            for file in sorted(files):
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    self._load_script(file_path)

        resolved = {}
        for reference in self.definitions:
            try:
                card_def = self._resolve(reference, resolved, [])
                self._add_card(reference, card_def)
            except Exception as e:
                error = f"{reference}: {e}"
                self.last_errors.append(error)
                logging.error("[Scripts] Failed to resolve card %s", error)
        
        logging.info(f"[Scripts] Successfully loaded {len(self.cards)} card scripts.")
        return self.cards

    def _resolve(self, reference, resolved, chain):
        """Resolve parent definitions independently of filesystem order."""
        if reference in resolved:
            return resolved[reference]
        if reference in chain:
            raise ValueError("Reprint inheritance cycle: " + " -> ".join(chain + [reference]))
        if reference not in self.definitions:
            raise ValueError(f"Missing reprint parent: {reference}")
        definition = self.definitions[reference]
        if getattr(definition, "inherits", None) is not None:
            parent = self._resolve(definition.inherits, resolved, chain + [reference])
            definition = definition.resolve(parent)
        resolved[reference] = definition
        return definition

    def _add_card(self, reference, card_def):
        """Publish a resolved definition as a server card model."""
        archetype = card_def.to_archetype_dict()
        guid, key, attrs = archetype["guid"], archetype["key"], archetype["attributes"]
        c_type = attrs.get(str(AttrID.CARD_TYPE.value), {}).get("value", CardType.UNSET)
        model = PokemonCard if c_type == CardType.POKEMON else Card
        card = model(guid, key, attrs, archetype.get("display_name"),
                     archetype.get("searchable_by", []), getattr(card_def, "subtypes", []))
        self.cards.append(card)
        self.cards_by_guid[guid] = card
        self.cards_by_key[key] = card
        self.cards_by_stem[reference.rsplit("/", 1)[-1]] = guid

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
                reference = os.path.splitext(rel_path)[0].replace(os.path.sep, "/")
                self.definitions[reference] = module.card
            else:
                logging.warning(f"[Scripts] Script {file_path} does not define a 'card' object.")
                
        except Exception as e:
            self.last_errors.append(f"{file_path}: {e}")
            logging.error(f"[Scripts] Failed to load script {file_path}: {e}")

# Global loader instance
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__))
loader = ScriptLoader(SCRIPTS_DIR)
