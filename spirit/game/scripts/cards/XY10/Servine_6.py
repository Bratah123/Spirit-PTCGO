"""STUB: effect not implemented — do not guess mechanics.
Servine (XY10 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9c8d9bc-05f7-5adf-9eeb-35eaf67b657c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    display_name="Servine",
    searchable_by=["Servine", "Stage 1", "Servine"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Serpentine Strangle",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)