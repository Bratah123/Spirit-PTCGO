"""STUB: effect not implemented — do not guess mechanics.
Bergmite (XY11 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98dfccbd-54a7-5347-9c8e-3da380b572a2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    display_name="Bergmite",
    searchable_by=["Bergmite", "Basic", "Bergmite"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=712,
    abilities=[
        Attack(
            title="Ice Block",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)