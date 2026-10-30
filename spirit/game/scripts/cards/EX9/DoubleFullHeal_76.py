from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect


def _active_has_special_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return bool(active) and bool(active.get_attribute(AttrID.SPECIAL_CONDITIONS))


card = ItemCardDef(
    guid="be9a1491-756a-559c-aec4-c46fd9aa3d17",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    condition=_active_has_special_condition,
    effect=cure_conditions_effect(),
)
