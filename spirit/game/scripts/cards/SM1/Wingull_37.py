from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _roost(ctx):
    """Heal 30 damage from this Pokemon. It can't retreat during your next turn."""
    await ctx.heal(30, ctx.attacker)
    ctx.lock_retreat(ctx.attacker, through_turn=ctx.session.turn_state.turn_number + 2)


card = PokemonCardDef(
    guid="c55c3b3d-15c7-5e1b-95d7-a86c95b18243",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    display_name="Wingull",
    searchable_by=["Wingull", "Basic", "Wingull"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=278,
    abilities=[
        Attack(
            title="Roost",
            game_text="Heal 30 damage from this Pok\u00e9mon. It can't retreat during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_roost,
        ),
    ],
)