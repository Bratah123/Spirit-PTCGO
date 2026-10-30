"""Wired DP1 trainer."""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import night_pokemon_center

card = ItemCardDef(
    guid="5b868f01-dfbf-55da-91d7-65bbc3face46",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightPokemonCenter.Name",
    display_name="Night Pokémon Center",
    searchable_by=["Night Pok\u00e9mon Center", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=night_pokemon_center()
)
