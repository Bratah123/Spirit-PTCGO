from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spelunk(ctx):
    """Look at the top 3 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(3)


card = PokemonCardDef(
    guid="b350eef9-2dbd-5abb-85f9-92844ef03c42",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic", "AlolanDiglett"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=50,
    abilities=[
        Attack(
            title="Spelunk",
            game_text="Look at the top 3 cards of your deck and put them back in any order.",
            cost={},
            effect=_spelunk,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)