"""STUB: effect not implemented — do not guess mechanics.
Charmeleon (DP3 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="2641bda4-6f5e-5a1a-ae9f-b46568273807",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Flare Tail",
            game_text="Flip a coin. If heads, discard a Fire Energy attached to Charmeleon and this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)