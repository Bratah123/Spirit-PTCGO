from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect


def _active_has_special_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return bool(active) and bool(active.get_attribute(AttrID.SPECIAL_CONDITIONS))


card = ItemCardDef(
    guid="f3e6769c-7baa-58f8-b2a6-fe2be6793e39",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    condition=_active_has_special_condition,
    effect=cure_conditions_effect(),
)
