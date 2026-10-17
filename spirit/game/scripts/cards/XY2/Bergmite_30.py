"""STUB: effect not implemented — do not guess mechanics.
Bergmite (XY2 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7b4c04f-864d-5727-b69a-a443d80661f8",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    display_name="Bergmite",
    searchable_by=["Bergmite", "Basic", "Bergmite"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=712,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)