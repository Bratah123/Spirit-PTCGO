"""STUB: effect not implemented — do not guess mechanics.
Shellder (DP3 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30cd9d6f-4f8e-56cd-bc4c-97efa64c47e4",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    display_name="Shellder",
    searchable_by=["Shellder", "Basic", "Shellder"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=90,
    abilities=[
        Attack(
            title="Shell Rest",
            game_text="Remove 2 damage counters from Shellder.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tongue Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)