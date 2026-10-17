"""STUB: effect not implemented — do not guess mechanics.
Swirlix (XY0 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0583c07c-66e8-5afb-96f7-8c16f2fe9933",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic", "Swirlix"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=684,
    abilities=[
        Attack(
            title="Draining Kiss",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)