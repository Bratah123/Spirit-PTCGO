from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def headbutt_tantrum(ctx):
    """On play from hand to Bench: you may put 1 damage counter on 1 of
    your opponent's Pokémon."""
    if not await ctx.ask_yes_no(
        "Put 1 damage counter on 1 of your opponent's Pokémon?"
    ):
        return
    await ctx.place_damage_counters(1)


card = PokemonCardDef(
    guid="e3800492-f270-5d13-8cb3-7b695565caea",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    display_name="Galarian Zigzagoon",
    searchable_by=["Galarian Zigzagoon", "Basic", "GalarianZigzagoon"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=263,
    abilities=[
        Ability(
            title="Headbutt Tantrum",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=headbutt_tantrum,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)