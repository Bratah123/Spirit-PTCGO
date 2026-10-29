from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def glance(ctx):
    """Look at the top card of your opponent's deck."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.present_card_choice(
        top[0], "Top card of your opponent's deck", ["OK"])


card = PokemonCardDef(
    guid="4a7659c5-0e60-5cfe-ab0a-00833959bba2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat", "Basic", "Patrat"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Attack(
            title="Glance",
            game_text="Look at the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=glance,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)