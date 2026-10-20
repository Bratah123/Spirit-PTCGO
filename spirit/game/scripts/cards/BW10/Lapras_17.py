from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sugary_sprinkles(ctx):
    """Heal 30 damage from each of your Benched Pokemon."""
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="af8d4c0e-3c41-5d66-9e1d-865d441b0793",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Cleanse Away",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=sugary_sprinkles,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)