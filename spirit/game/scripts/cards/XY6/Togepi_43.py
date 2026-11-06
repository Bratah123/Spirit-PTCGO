from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _sweet_kiss(ctx):
    """Printed damage; your opponent draws a card."""
    await ctx.deal_damage()
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="dc01572f-9c45-55ed-8569-59c06a294e9c",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=175,
    abilities=[
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent draws a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_sweet_kiss,
        ),
    ],
)