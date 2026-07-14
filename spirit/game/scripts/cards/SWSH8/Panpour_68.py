from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def pry(ctx):
    """10 damage. Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="afbb8bd3-1c72-572e-8e73-452af8232207",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    display_name="Panpour",
    searchable_by=["Panpour", "Basic", "Panpour"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=515,
    abilities=[
        Attack(
            title="Pry",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=pry,
        ),
    ],
)