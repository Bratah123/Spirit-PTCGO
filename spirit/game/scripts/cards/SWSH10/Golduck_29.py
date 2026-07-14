from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def entangled_dive(ctx):
    """Discard each player's Active Pokémon and all attached cards; each
    player chooses a new Active first (mine, then the opponent's)."""
    old_actives = {}
    need_promotion = []
    for pid in (ctx.player_id, ctx.opponent_id):
        is_mine = pid == ctx.player_id
        active = ctx.my_active() if is_mine else ctx.opponent_active()
        if active is None:
            continue
        bench = ctx.my_bench() if is_mine else ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon", player_id=pid
            )
            await ctx.switch_active(pid, target)
        else:
            need_promotion.append(pid)
        old_actives[pid] = active

    for active in old_actives.values():
        await ctx.discard_cards(full_stack(active))

    for pid in need_promotion:
        async def _promote(pid=pid):
            if not await ctx.session._promote_new_active(pid):
                opponent = ctx.opponent_id if pid == ctx.player_id else ctx.player_id
                screen_name = ctx.session.players[pid].screen_name
                await ctx.session.end_game(
                    opponent, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="d90ddaef-aaa2-58a0-8ba7-f4609d3d9680",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Entangled Dive",
            game_text="Discard each player's Active Pok\u00e9mon and all attached cards. (You choose a new Active Pok\u00e9mon first.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=entangled_dive,
        ),
    ],
)