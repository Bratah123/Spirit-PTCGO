"""STUB: effect not implemented — do not guess mechanics.
Quilladin (XY0 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35ed6de8-51a1-513f-a6c9-02bd2f6d37ac",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    display_name="Quilladin",
    searchable_by=["Quilladin", "Stage 1", "Quilladin"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Needle Arm",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)