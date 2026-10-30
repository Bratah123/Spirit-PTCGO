from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import magnifier_passive


card = PokemonToolCardDef(
    guid="8e7c9327-face-5c1f-9331-1083aa0b9a10",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Magnifier.Name",
    display_name="Magnifier",
    searchable_by=["Magnifier", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=101,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    passive=magnifier_passive,
)
