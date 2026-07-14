from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, count_prizes_remaining


async def victory_symbol(ctx):
    """No damage. If you have only 1 Prize card remaining, you win the game."""
    if count_prizes_remaining("mine")(ctx) == 1:
        await ctx.win_game("Victory Symbol")

card = PokemonCardDef(
    guid="d03cee67-a14e-52a4-a653-e862bf65533a",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown V",
    searchable_by=["Unown V", "Basic", "V", "UnownV"],
    subtypes=["Basic", "V"],
    collector_number=176,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=201,
    abilities=[
        Attack(
            title="Shady Stamp",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Victory Symbol",
            game_text="If you use this attack when you have only 1 Prize card remaining, you win this game.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=victory_symbol,
        ),
    ],
)