from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _return(ctx):
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Draw cards until you have 5 cards in your hand?"):
        await ctx.draw_until(5)

card = PokemonCardDef(
    guid="382c1054-c839-5fd1-afc1-6f04f5714e2e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic", "Furfrou"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 5 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_return,
        ),
    ],
)
