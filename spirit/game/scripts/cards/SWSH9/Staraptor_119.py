from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def strong_breeze(ctx):
    """Your opponent shuffles their Active Pokemon and all attached cards into their deck."""
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


spinning_bird = self_energy_discard_attack(count=2)

card = PokemonCardDef(
    guid="973a434c-a358-53bb-9edb-b6578dc8aeec",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=119,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Strong Breeze",
            game_text="Your opponent shuffles their Active Pok\u00e9mon and all attached cards into their deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=strong_breeze,
        ),
        Attack(
            title="Spinning Bird",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            effect=spinning_bird,
        ),
    ],
)