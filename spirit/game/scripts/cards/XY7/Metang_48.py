"""STUB: effect not implemented — do not guess mechanics.
Metang (XY7 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5ce68d6-6a06-5422-bc58-4cdc5a3eeab2",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Bullet Punch",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)