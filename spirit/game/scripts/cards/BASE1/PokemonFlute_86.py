from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_flute, pokemon_flute_condition


card = ItemCardDef(
    guid="c0600115-ca94-5116-8c10-f7105ac806f4",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFlute.Name",
    display_name="Pokémon Flute",
    searchable_by=["Pok\u00e9mon Flute"],
    subtypes=[],
    collector_number=86,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=pokemon_flute_condition,
    effect=pokemon_flute,
)
