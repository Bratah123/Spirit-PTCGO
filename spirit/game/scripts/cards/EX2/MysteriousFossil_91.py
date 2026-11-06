from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="342a3e62-e836-5b30-bf75-f44ce27ae012",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
