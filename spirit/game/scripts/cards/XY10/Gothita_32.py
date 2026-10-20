"""STUB: effect not implemented — do not guess mechanics.
Gothita (XY10 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a34b8d60-ffc5-535c-9f7c-8e594e0d06e8",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic", "Gothita"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=574,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)