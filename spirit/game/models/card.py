import json
import hashlib
from typing import Any, Optional, Union
from spirit.game.attributes import AttrID, CardType, TrainerType, PokemonStage, PokemonTypes, Rarities, ProductType

def safe_int(value: Any, default: int = 0) -> int:
    """Safely converts a value to an integer, handling None and non-convertible types."""
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

class Card:
    def __init__(
        self, 
        guid: str, 
        key: str, 
        attributes: Optional[dict[str, Any]] = None,
        display_name: Optional[str] = None,
        searchable_by: Optional[list[str]] = None,
        subtypes: Optional[list[str]] = None
    ):
        self.guid = guid
        self.key = key
        self.attributes = attributes or {}
        self.display_name = display_name
        self.searchable_by = searchable_by or []
        self.subtypes = subtypes or []

    def get_attribute_value(self, attr_id: Union[int, AttrID], default: Any = None) -> Any:
        attr = self.attributes.get(str(attr_id.value if isinstance(attr_id, AttrID) else attr_id))
        if attr:
            val = attr.get("value")
            return val if val is not None else default
        return default

    def to_archetype_attributes(self, download_key: str) -> dict[str, Any]:
        """
        Returns a dictionary of attributes formatted for the Warg Protocol,
        ensuring all mandatory fields for rendering are present.
        """
        final_attrs = dict(self.attributes)

        # 1. Map to the active download key (CRITICAL for SetCache)
        final_attrs[str(AttrID.SET_CACHE_KEY.value)] = {
            "type": "string", "value": download_key
        }
        final_attrs[str(AttrID.EXPANSION.value)] = {
            "type": "string", "value": download_key
        }

        # Force Name (Attribute 10140) to be a JSON LocalizableText object
        name_val = self.get_attribute_value(AttrID.NAME)
        if isinstance(name_val, str) and name_val.startswith('{'):
            final_attrs[str(AttrID.NAME.value)] = {"type": "json", "value": name_val}
        else:
            token = str(name_val) if name_val is not None else "ids_card_name_spirit"
            final_attrs[str(AttrID.NAME.value)] = {
                "type": "json", "value": json.dumps({"id": token})
            }

        # 2. Collector Number (CRITICAL for rendering/filenames)
        coll_num = self.get_attribute_value(AttrID.COLLECTOR_NUMBER)
        if coll_num is None:
            key_parts = self.key.split('_')
            if len(key_parts) > 1 and key_parts[-1].isdigit():
                coll_num = safe_int(key_parts[-1])
            else:
                coll_num = (int(hashlib.md5(self.guid.encode()).hexdigest(), 16) % 900) + 1
        
        final_attrs[str(AttrID.COLLECTOR_NUMBER.value)] = {
            "type": "int", "value": safe_int(coll_num)
        }

        # Force Card Image Asset Name (Attribute 10510)
        padded_num = str(safe_int(coll_num)).zfill(3)
        final_attrs[str(AttrID.IMAGE_URL.value)] = {
            "type": "string", "value": padded_num
        }

        # 3. Mandatory technical attributes
        # Product Type (Attribute 10540) - ALWAYS "Singles" (26) for cards
        final_attrs[str(AttrID.PRODUCT_TYPE.value)] = {
            "type": "int", "value": ProductType.SINGLES.value
        }

        # Collection ID (Attribute 200000)
        if str(AttrID.COLLECTION_ID.value) not in final_attrs:
            final_attrs[str(AttrID.COLLECTION_ID.value)] = {
                "type": "string", "value": str(self.guid)
            }
        else:
            final_attrs[str(AttrID.COLLECTION_ID.value)]["type"] = "string"
            final_attrs[str(AttrID.COLLECTION_ID.value)]["value"] = str(final_attrs[str(AttrID.COLLECTION_ID.value)]["value"])

        # 4. Card Type Specific Attributes
        card_type_raw = self.get_attribute_value(AttrID.CARD_TYPE, CardType.UNSET)
        card_type_int = safe_int(card_type_raw, CardType.UNSET)
        
        if card_type_int != CardType.UNSET:
            final_attrs[str(AttrID.CARD_TYPE.value)] = {
                "type": "int", "value": card_type_int
            }

        if card_type_int == CardType.POKEMON:
            # Pokemon Stage (Attribute 200540) - Default to "Basic" (0) if missing
            if str(AttrID.STAGE.value) not in final_attrs:
                final_attrs[str(AttrID.STAGE.value)] = {
                    "type": "int", "value": PokemonStage.BASIC.value
                }
            if str(AttrID.PIE_ABILITIES.value) not in final_attrs:
                final_attrs[str(AttrID.PIE_ABILITIES.value)] = {
                    "type": "json", "value": "[]"
                }

        elif card_type_int == CardType.TRAINER:
            # Trainer Type (Attribute 200270) - MANDATORY for grouping
            t_type_raw = self.get_attribute_value(AttrID.TRAINER_TYPE)
            
            if t_type_raw is None:
                # Improved heuristic: check token for type
                token_lower = str(name_val).lower() if name_val is not None else ""
                if any(x in token_lower for x in ["stadium", "seaof", "roughseas", "gym"]):
                    t_type = TrainerType.STADIUM
                elif "supporter" in token_lower:
                    t_type = TrainerType.SUPPORTER
                else:
                    t_type = TrainerType.ITEM
            else:
                t_type = safe_int(t_type_raw, TrainerType.ITEM)
            
            final_attrs[str(AttrID.TRAINER_TYPE.value)] = {
                "type": "int", "value": t_type if isinstance(t_type, int) else t_type.value
            }

        elif card_type_int == CardType.ENERGY:
            if str(AttrID.ENERGY_INFO.value) not in final_attrs:
                final_attrs[str(AttrID.ENERGY_INFO.value)] = {
                    "type": "json", "value": "{\"options\": []}"
                }

        # 5. Mandatory facet components
        # Rarity (Attribute 200550)
        r_val_raw = self.get_attribute_value(AttrID.RARITY, Rarities.Common)
        final_attrs[str(AttrID.RARITY.value)] = {
            "type": "int", "value": safe_int(r_val_raw, Rarities.Common.value)
        }

        # 6. Apply Foil attributes if present, otherwise default to 0
        foil_mask = self.get_attribute_value(AttrID.FOIL_MASK)
        if foil_mask is not None:
            final_attrs[str(AttrID.FOIL_MASK.value)] = {"type": "int", "value": safe_int(foil_mask)}
        else:
            final_attrs[str(AttrID.FOIL_MASK.value)] = {"type": "int", "value": 0}

        foil_effect = self.get_attribute_value(AttrID.FOIL_EFFECT)
        if foil_effect is not None:
            final_attrs[str(AttrID.FOIL_EFFECT.value)] = {"type": "int", "value": safe_int(foil_effect)}
        else:
            final_attrs[str(AttrID.FOIL_EFFECT.value)] = {"type": "int", "value": 0}

        foil_effects = self.get_attribute_value(AttrID.FOIL_EFFECTS)
        if foil_effects is not None:
            final_attrs[str(AttrID.FOIL_EFFECTS.value)] = {"type": "json", "value": json.dumps(foil_effects) if isinstance(foil_effects, list) else str(foil_effects)}
        else:
            final_attrs[str(AttrID.FOIL_EFFECTS.value)] = {"type": "json", "value": "[]"}

        foil_intensity = self.get_attribute_value(AttrID.FOIL_INTENSITY)
        if foil_intensity is not None:
            final_attrs[str(AttrID.FOIL_INTENSITY.value)] = {"type": "int", "value": safe_int(foil_intensity)}
        elif foil_mask is not None or foil_effect is not None:
            # Default intensity for foil cards if not specified
            final_attrs[str(AttrID.FOIL_INTENSITY.value)] = {"type": "int", "value": 100}
        else:
            final_attrs[str(AttrID.FOIL_INTENSITY.value)] = {"type": "int", "value": 0}

        # 7. Ensure EVOLUTION_LOGIC_NAME (200630 / Card Name) is ALWAYS populated to prevent client null key crashes on attachments
        if str(AttrID.EVOLUTION_LOGIC_NAME.value) not in final_attrs:
            name_val = self.get_attribute_value(AttrID.NAME)
            if name_val is not None:
                name_str = str(name_val)
                if isinstance(name_val, str) and name_val.startswith('{'):
                    try:
                        name_data = json.loads(name_val)
                        name_str = name_data.get("id", name_val)
                    except Exception:
                        pass
                name_part = name_str.split(".")[-2] if "direwolfdigital" in name_str else name_str
            else:
                name_part = "spirit_card"
            final_attrs[str(AttrID.EVOLUTION_LOGIC_NAME.value)] = {
                "type": "string", "value": name_part
            }

        return final_attrs

class PokemonCard(Card):
    def __init__(
        self, 
        guid: str, 
        key: str, 
        attributes: Optional[dict[str, Any]] = None,
        display_name: Optional[str] = None,
        searchable_by: Optional[list[str]] = None,
        subtypes: Optional[list[str]] = None
    ):
        super().__init__(guid, key, attributes, display_name, searchable_by, subtypes)

    @property
    def hp(self) -> int:
        return safe_int(self.get_attribute_value(AttrID.HP), 100)

    @property
    def stage(self) -> int:
        return safe_int(self.get_attribute_value(AttrID.STAGE), PokemonStage.BASIC.value)

    @property
    def pokemon_types(self) -> list[int]:
        val = self.get_attribute_value(AttrID.POKEMON_TYPES)
        if val is None:
            return [PokemonTypes.COLORLESS.value]
        if isinstance(val, list):
            return [safe_int(v) for v in val]
        return [safe_int(val)]

    @property
    def retreat_cost(self) -> int:
        return safe_int(self.get_attribute_value(AttrID.RETREAT_COST), 1)

    def to_archetype_attributes(self, download_key: str) -> dict[str, Any]:
        # We start with the base card attributes
        final_attrs = super().to_archetype_attributes(download_key)

        # Force Card Type to Pokemon (0)
        final_attrs[str(AttrID.CARD_TYPE.value)] = {
            "type": "int", "value": CardType.POKEMON.value
        }

        # Mandatory Pokemon Rendering/Stat Attributes
        # HP (200490 in client)
        if str(AttrID.HP.value) not in final_attrs:
            final_attrs[str(AttrID.HP.value)] = {"type": "int", "value": self.hp}

        # Stage (200540)
        if str(AttrID.STAGE.value) not in final_attrs:
            final_attrs[str(AttrID.STAGE.value)] = {"type": "int", "value": self.stage}

        # Types (200570) - Client expects a JSON array of integers
        if str(AttrID.POKEMON_TYPES.value) not in final_attrs:
            types = self.pokemon_types
            final_attrs[str(AttrID.POKEMON_TYPES.value)] = {
                "type": "json", "value": json.dumps(types)
            }

        # Retreat Cost (200800 in client)
        if str(AttrID.RETREAT_COST.value) not in final_attrs:
            final_attrs[str(AttrID.RETREAT_COST.value)] = {"type": "int", "value": self.retreat_cost}

        # Family ID (200260) - MANDATORY for EvolutionsRenderUtil to not crash
        family_id = safe_int(self.get_attribute_value(AttrID.FAMILY_ID), 0)
        final_attrs[str(AttrID.FAMILY_ID.value)] = {"type": "int", "value": family_id}

        # Defaults for Weakness/Resistance if missing
        if str(AttrID.WEAKNESS_TYPES.value) not in final_attrs:
            final_attrs[str(AttrID.WEAKNESS_TYPES.value)] = {"type": "json", "value": "[]"}
        if str(AttrID.RESISTANCE_TYPES.value) not in final_attrs:
            final_attrs[str(AttrID.RESISTANCE_TYPES.value)] = {"type": "int", "value": PokemonTypes.UNSET.value}

        # Handle operators and amounts
        weakness_types_val = final_attrs.get(str(AttrID.WEAKNESS_TYPES.value), {}).get("value")
        if weakness_types_val and weakness_types_val != "[]":
            if str(AttrID.WEAKNESS_OPERATOR.value) not in final_attrs:
                final_attrs[str(AttrID.WEAKNESS_OPERATOR.value)] = {"type": "string", "value": "x"}
            if str(AttrID.WEAKNESS_AMOUNT.value) not in final_attrs:
                final_attrs[str(AttrID.WEAKNESS_AMOUNT.value)] = {"type": "int", "value": 2}

        resistance_type_val = final_attrs.get(str(AttrID.RESISTANCE_TYPES.value), {}).get("value")
        if resistance_type_val and resistance_type_val != PokemonTypes.UNSET.value:
            if str(AttrID.RESISTANCE_OPERATOR.value) not in final_attrs:
                final_attrs[str(AttrID.RESISTANCE_OPERATOR.value)] = {"type": "string", "value": "-"}
            if str(AttrID.RESISTANCE_AMOUNT.value) not in final_attrs:
                final_attrs[str(AttrID.RESISTANCE_AMOUNT.value)] = {"type": "int", "value": 30}

        # Pie Abilities (200740) - Mandatory for the renderer to not crash
        if str(AttrID.PIE_ABILITIES.value) not in final_attrs:
            final_attrs[str(AttrID.PIE_ABILITIES.value)] = {
                "type": "json", "value": "[]"
            }

        return final_attrs
