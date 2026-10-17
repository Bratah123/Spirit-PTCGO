"""STUB: effect not implemented — do not guess mechanics.
Petilil (XY9 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a6fe586-2a2c-5788-8a49-e487551e6c7e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil", "Basic", "Petilil"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=548,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)