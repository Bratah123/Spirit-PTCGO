"""STUB: effect not implemented — do not guess mechanics.
M Beedrill-EX (Promo_XY #XY158): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d5f1a5b-d016-5c03-b005-2eb98b746e31",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBeedrillEX.Name",
    display_name="M Beedrill-EX",
    searchable_by=["M Beedrill-EX", "MEGA", "EX", "MBeedrillEX"],
    subtypes=["MEGA", "EX"],
    collector_number=158,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name",
    family_id=15,
    abilities=[
        Attack(
            title="Hazard Stinger",
            game_text="Discard all Energy attached to this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned. Put 4 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)