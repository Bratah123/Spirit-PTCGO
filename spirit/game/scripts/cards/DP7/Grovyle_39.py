"""STUB: effect not implemented — do not guess mechanics.
Grovyle (DP7 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1a007a90-a164-5564-83f1-e174770acfe0",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Tail Shake",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)