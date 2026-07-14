from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import AttrID, Rarities


def _panic_mask_shield(calc, carrier):
    if calc.target is not carrier:
        return False
    attacker = calc.attacker
    if attacker is None:
        return False
    return attacker.get_attribute(AttrID.HP, 0) <= 40


card = PokemonToolCardDef(
    guid="0ed49119-8252-5cd1-826a-ef12e56e80fb",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PanicMask.Name",
    display_name="Panic Mask",
    searchable_by=["Panic Mask", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=165,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    passive=prevent_damage_when(_panic_mask_shield),
)
