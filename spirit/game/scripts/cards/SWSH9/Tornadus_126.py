from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def sudden_cyclone(ctx):
    """On play from hand: you may have your opponent switch their Active
    Pokémon with 1 of their Benched Pokémon."""
    if ctx.opponent_bench() and await ctx.ask_yes_no(
        "Have your opponent switch their Active Pokémon with 1 of their "
        "Benched Pokémon?"
    ):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="f5efc250-82e1-5a20-9ce9-d8544857ef02",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Ability(
            title="Sudden Cyclone",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=sudden_cyclone,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)