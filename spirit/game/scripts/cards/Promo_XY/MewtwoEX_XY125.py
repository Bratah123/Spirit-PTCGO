"""STUB: effect not implemented — do not guess mechanics.
Mewtwo-EX (Promo_XY #XY125): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd86f173-aea9-5bc1-b199-86708b46c40c",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=125,
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
            title="Photon Wave",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)