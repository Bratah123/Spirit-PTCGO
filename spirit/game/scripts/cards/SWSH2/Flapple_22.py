from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def apple_drop(ctx):
    if not await ctx.ask_yes_no(
            "Put 2 damage counters on 1 of your opponent's Pokémon?"):
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    dealt = await ctx.deal_damage(20, target=target, as_counters=True)
    if dealt <= 0:
        return
    pokemon = ctx.source
    was_active = pokemon is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def acid_spray(ctx):
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Acid Spray"))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose Energy to discard from the Defending Pokémon")

card = PokemonCardDef(
    guid="da729e0f-309f-50ef-aafe-9c34630e6e10",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Apple Drop",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If you placed any damage counters in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=apple_drop,
        ),
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=acid_spray,
        ),
    ],
)