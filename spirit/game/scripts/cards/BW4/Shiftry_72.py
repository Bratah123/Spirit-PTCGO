from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.session.effects import full_stack


async def _giant_fan(ctx):
    """On evolve from hand: you may flip a coin. If heads, the opponent
    shuffles 1 of their Pokémon (your choice) and all attached cards into
    their deck."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    if not await ctx.ask_yes_no("Use Giant Fan? Flip a coin."):
        return
    results = await ctx.flip_coins(1, "Giant Fan")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon to shuffle into their deck")
    if target is None:
        return
    was_active = target is ctx.opponent_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen_name = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="ab83561a-12cc-5dbf-aa6b-cd1c7da4f2b7",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=72,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Giant Fan",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. Your opponent shuffles that Pok\u00e9mon and all cards attached to it into his or her deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_giant_fan,
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)