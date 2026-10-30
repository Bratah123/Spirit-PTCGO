from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_center
from spirit.game.card_effects.support_common import requires_damaged_pokemon


card = ItemCardDef(
    guid="e9728209-ae39-5204-ae97-b70869663e0e",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=85,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=pokemon_center,
)
