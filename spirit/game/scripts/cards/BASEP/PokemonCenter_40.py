from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_center
from spirit.game.card_effects.support_common import requires_damaged_pokemon


card = ItemCardDef(
    guid="58d8b88f-a7bc-5d17-9f78-bf45c9eb1306",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=40,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    condition=requires_damaged_pokemon(),
    effect=pokemon_center,
)
