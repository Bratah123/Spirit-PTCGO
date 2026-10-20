from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import full_stack


async def _deck_and_cover(ctx):
    """Printed damage; Defending is Paralyzed and Poisoned; shuffle this
    Pokémon and all attached cards into your deck."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)
    pokemon = ctx.attacker
    was_active = pokemon is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="ce916be1-a0d8-5def-9e55-1604833ea30e",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Accelgor"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Deck and Cover",
            game_text="The Defending Pok\u00e9mon is now Paralyzed and Poisoned. Shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_deck_and_cover,
        ),
    ],
)