from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


async def fidget(ctx):
    """Shuffle your deck."""
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="16c75ec8-108c-56d4-b64d-0fa6ede24fbf",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksMankey.Name",
    display_name="Brock's Mankey",
    searchable_by=["Brock's Mankey", "Basic", "BrocksMankey"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Fidget",
            game_text="Shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fidget,
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 40 damage minus 10 damage for each damage counter on Brock's Mankey.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="-",
            effect=damage_per(damage_counters_on("self"), -10, base=40),
        ),
    ],
)
