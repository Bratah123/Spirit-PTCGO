"""Wired DP1 trainer."""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import pokedex_handy

card = ItemCardDef(
    guid="5d41809b-f503-5ebc-a5db-8d07eb58bfea",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokedexHANDY910is.Name",
    display_name="Pokédex HANDY910is",
    searchable_by=["Pok\u00e9dex HANDY910is", "Item"],
    subtypes=["Item"],
    collector_number=111,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=pokedex_handy()
)
