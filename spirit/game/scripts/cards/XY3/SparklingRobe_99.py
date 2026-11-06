from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import condition_immunity_passive

card = PokemonToolCardDef(
    guid="f05087b3-ca20-5ec4-b850-b5db64d3d28b",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SparklingRobe.Name",
    display_name="Sparkling Robe",
    searchable_by=["Sparkling Robe", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive()
)
