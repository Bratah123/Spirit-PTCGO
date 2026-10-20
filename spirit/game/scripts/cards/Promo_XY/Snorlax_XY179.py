"""STUB: effect not implemented — do not guess mechanics.
Snorlax (Promo_XY #XY179): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d6f40549-8270-5144-bfcd-9dfedb09e011",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=179,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Immunity",
            game_text="This Pok\u00e9mon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pok\u00e9mon.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)