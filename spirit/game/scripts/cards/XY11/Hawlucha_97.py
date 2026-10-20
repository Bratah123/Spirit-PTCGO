from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.attacks_common import flip_damage


async def sudden_cyclone(ctx):
    """On play from hand: you may have your opponent switch their Active
    Pokémon with 1 of their Benched Pokémon."""
    if ctx.opponent_bench() and await ctx.ask_yes_no(
        "Have your opponent switch their Active Pokémon with 1 of their "
        "Benched Pokémon?"
    ):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="c732ce73-0903-5a00-8e5e-bba9af568199",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Ability(
            title="Sudden Cyclone",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=sudden_cyclone,
        ),
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)