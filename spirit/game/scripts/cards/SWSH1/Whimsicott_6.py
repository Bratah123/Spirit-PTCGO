from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def cotton_ride(ctx):
    """Flip a coin. If heads, opponent shuffles their Active and all
    attached cards into their deck."""
    heads = (await ctx.flip_coins(1, "Cotton Ride"))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="a9813aa3-4044-50a3-88d4-ef9b6646f22f",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Cotton Ride",
            game_text="Flip a coin. If heads, your opponent shuffles their Active Pok\u00e9mon and all attached cards into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cotton_ride,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
        ),
    ],
)