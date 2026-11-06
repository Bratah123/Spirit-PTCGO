from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def mischief(ctx):
    await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="1bc25616-cd70-53da-a75d-69df913ff27c",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic", "Mankey"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Mischief",
            game_text="Shuffle your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischief,
        ),
        Attack(
            title="Anger",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage; if tails, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
