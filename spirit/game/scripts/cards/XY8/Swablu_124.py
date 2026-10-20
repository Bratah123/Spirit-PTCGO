"""STUB: effect not implemented — do not guess mechanics.
Swablu (XY8 #124): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a829dce5-c3f5-505b-af31-a1e92df13843",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu",
    searchable_by=["Swablu", "Basic", "Swablu"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=333,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Heal 20 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)