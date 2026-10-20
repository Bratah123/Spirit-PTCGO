"""STUB: effect not implemented — do not guess mechanics.
Toxicroak-EX (XY2 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="ecc7dfe1-f2bb-53e4-90cc-a1b39368e9f8",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxicroakEX.Name",
    display_name="Toxicroak-EX",
    searchable_by=["Toxicroak-EX", "Basic", "EX", "ToxicroakEX"],
    subtypes=["Basic", "EX"],
    collector_number=41,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=454,
    abilities=[
        Attack(
            title="Triple Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 3 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Smash Uppercut",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=feint,
        ),
    ],
)