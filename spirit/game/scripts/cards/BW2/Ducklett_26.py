from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def roost(ctx):
    """Heal 40. This Pokémon can't retreat during your next turn."""
    await ctx.heal(40, ctx.attacker)
    ctx.lock_retreat(
        ctx.attacker,
        through_turn=ctx.session.turn_state.turn_number + 2,
    )


card = PokemonCardDef(
    guid="0cbee559-53ed-50ec-8b78-3996438d41d8",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    display_name="Ducklett",
    searchable_by=["Ducklett", "Basic", "Ducklett"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=580,
    abilities=[
        Attack(
            title="Roost",
            game_text="Heal 40 damage from this Pok\u00e9mon. This Pok\u00e9mon can't retreat during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=roost,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 2},
            damage=20,
        ),
    ],
)
