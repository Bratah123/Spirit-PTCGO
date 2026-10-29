from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.session.passives import effective_max_hp


def _malasada_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return active is not None and (
        effective_max_hp(board, active) > active.get_attribute(AttrID.HP, 0)
        or bool(active.get_attribute(AttrID.SPECIAL_CONDITIONS)))


async def _big_malasada(ctx):
    """Heal 20 damage and remove a Special Condition from your Active Pokemon."""
    active = ctx.my_active()
    if active is None:
        return
    await ctx.heal(20, active)
    present = set(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    options = [(name, cond) for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()
               if name in present]
    if not options:
        return
    if len(options) == 1:
        cond = options[0][1]
    else:
        pick = await ctx.choose("Remove which Special Condition?",
                                [n for n, _ in options], use_panel=False)
        cond = options[pick if isinstance(pick, int) else 0][1]
    await ctx.cure_condition(active, cond)


card = ItemCardDef(
    guid="7a2c3aff-ac27-5a97-8ca0-7e239c97e5ee",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigMalasada.Name",
    display_name="Big Malasada",
    searchable_by=["Big Malasada", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_big_malasada,
    condition=_malasada_condition
)
