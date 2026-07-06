from spirit.game.card_effects.pokemon import ChoiceBeltPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    passive=ChoiceBeltPassive(),
    guid="3eae8ec5-aacb-5611-a172-5061eb03697e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBelt.Name",
    display_name="Choice Belt",
    searchable_by=["Choice Belt", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=211,
    set_code="SWSH10",
    rarity=Rarities.RareSecret
)
