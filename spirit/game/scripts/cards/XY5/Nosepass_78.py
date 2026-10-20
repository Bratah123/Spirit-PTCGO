"""STUB: effect not implemented — do not guess mechanics.
Nosepass (XY5 #78): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bab26bcf-5137-5987-a187-0ba219e2e56a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=299,
    abilities=[
        Attack(
            title="Stiffen",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)