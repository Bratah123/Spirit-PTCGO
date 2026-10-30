from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_center
from spirit.game.card_effects.support_common import requires_damaged_pokemon


card = ItemCardDef(
    guid="e54f6176-665d-5446-bb35-ed5e01b0b3cd",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=114,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=pokemon_center,
)
