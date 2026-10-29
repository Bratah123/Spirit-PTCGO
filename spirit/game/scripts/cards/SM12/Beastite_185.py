from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import beastite_passive

card = PokemonToolCardDef(
    guid="b3138bdc-662a-53b3-b63f-dbf4ab9d0414",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beastite.Name",
    display_name="Beastite",
    searchable_by=["Beastite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=185,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=beastite_passive,
)
