"""STUB: effect not implemented — do not guess mechanics.
Gyarados (XY7 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait

card = PokemonCardDef(
    guid="515531db-3a2d-5b98-9067-b53e6b6737a5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        ancient_trait('θ Double'),
        Attack(
            title="Full Retaliation",
            game_text="This attack does 30 more damage for each damage counter on each of your Benched Magikarp.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)