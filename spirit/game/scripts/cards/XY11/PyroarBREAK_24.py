"""STUB: effect not implemented — do not guess mechanics.
Pyroar BREAK (XY11 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="10219225-a107-533d-b2cf-3cc00e6f65d6",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PyroarBREAK.Name",
    display_name="Pyroar BREAK",
    searchable_by=["Pyroar BREAK", "BREAK", "PyroarBREAK"],
    subtypes=["BREAK"],
    collector_number=24,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Kaiser Tackle",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)