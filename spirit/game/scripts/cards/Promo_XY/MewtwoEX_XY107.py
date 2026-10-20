"""STUB: effect not implemented — do not guess mechanics.
Mewtwo-EX (Promo_XY #XY107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5a9533bd-4c69-5fab-83a4-4b88b7ad4efd",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=107,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Shatter Shot",
            game_text="This attack does 30 damage times the amount of Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Damage Change",
            game_text="Switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)