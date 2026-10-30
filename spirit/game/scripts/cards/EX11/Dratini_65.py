"""STUB: effect not implemented — do not guess mechanics.
Dratini δ (EX11 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59d63450-33d0-5802-ad99-f39d35e3fa9b",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini δ",
    searchable_by=["Dratini \u03b4", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=147,
    abilities=[
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Dratini does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=None,
        ),
    ],
)