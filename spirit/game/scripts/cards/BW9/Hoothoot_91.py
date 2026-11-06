from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def teatime(ctx):
    """Each player draws 2 cards."""
    await ctx.draw_cards(2, player_id=ctx.player_id)
    await ctx.draw_cards(2, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="b96e9f44-118e-5bc5-b8cb-76bcf54c0bf0",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Attack(
            title="Dual Draw",
            game_text="Each player draws 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=teatime,
        ),
    ],
)