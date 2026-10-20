"""STUB: effect not implemented — do not guess mechanics.
Raticate BREAK (XY9 #89): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="726d597a-c9ee-5041-8292-3e87e13483ea",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaticateBREAK.Name",
    display_name="Raticate BREAK",
    searchable_by=["Raticate BREAK", "BREAK", "RaticateBREAK"],
    subtypes=["BREAK"],
    collector_number=89,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Super Fang",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)