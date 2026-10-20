from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="3a29845f-e6a9-587f-b09a-0699b7455524",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    display_name="Vanillite",
    searchable_by=["Vanillite", "Basic", "Vanillite"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Snow Squall",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=feint,
        ),
    ],
)