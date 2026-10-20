"""STUB: effect not implemented — do not guess mechanics.
Wormadam (XY10 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="651919cd-d1e2-53cd-9219-6f69a1997b0d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name",
    display_name="Wormadam",
    searchable_by=["Wormadam", "Stage 1", "Wormadam"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Solar Ray",
            game_text="Heal 20 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Cutter",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)