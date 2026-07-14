from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def shiftadieu(ctx):
    """If the opponent's Active has any damage counters, put it and all
    attached cards into their hand."""
    target = ctx.defender
    if target is None:
        return
    if target.get_attribute(AttrID.HP, 0) >= ctx.max_hp(target):
        return
    if ctx.effects_blocked(target):
        return
    stack = full_stack(target)
    await ctx.put_in_hand(stack, reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)


async def nipping_cyclone(ctx):
    """130 damage; discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, 1)


card = PokemonCardDef(
    guid="475d1196-90d5-5551-af14-76a658ec78da",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Shiftadieu",
            game_text="If your opponent's Active Pok\u00e9mon has any damage counters on it, put it and all attached cards into your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=shiftadieu,
        ),
        Attack(
            title="Nipping Cyclone",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=nipping_cyclone,
        ),
    ],
)