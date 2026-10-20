from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


_gust = gust_attack()


async def _captivate(ctx):
    """Flip a coin. If heads, switch 1 of your opponent's Benched Pokemon with the Defending Pokemon."""
    results = await ctx.flip_coins(1, "Captivate")
    if results and results[0]:
        await _gust(ctx)


card = PokemonCardDef(
    guid="2a927def-f2f1-5099-b7e7-882686349d68",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=509,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_captivate,
        ),
    ],
)