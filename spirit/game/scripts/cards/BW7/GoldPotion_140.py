from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import heal_item


def _active_damaged(board, player_id):
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return active.get_attribute(AttrID.HP, 0) < active.attribute_originals.get(AttrID.HP.value, 0)


card = ItemCardDef(
    guid="361a42e7-0c15-53e1-828d-f278212fe518",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldPotion.Name",
    display_name="Gold Potion",
    searchable_by=["Gold Potion", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=140,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=heal_item(90, scope="active"),
    condition=_active_damaged
)
