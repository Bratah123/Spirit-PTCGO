from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.passives import effective_max_hp


def _damage_pump_condition(board, player_id, pokemon=None):
    mine = board.pokemon_in_play(player_id)
    if len(mine) < 2:
        return False
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in mine)


async def damage_pump(ctx):
    """Move up to 2 damage counters from 1 of your Pokemon to your others, any way you like."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to move damage counters from"
    )
    if source is None:
        return
    targets = [p for p in ctx.my_pokemon_in_play() if p is not source]
    if not targets:
        return
    await ctx.move_damage_counters(source, targets, max_count=2)


card = ItemCardDef(
    guid="d7949429-a9ba-5fc0-b1e9-6124b68e0c60",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DamagePump.Name",
    display_name="Damage Pump",
    searchable_by=["Damage Pump", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=damage_pump,
    condition=_damage_pump_condition
)
