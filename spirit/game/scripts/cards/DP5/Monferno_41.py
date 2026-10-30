"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_bonus


card = PokemonCardDef(
    guid="12c4145b-696c-501f-be4a-fea9a352223b",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    display_name="Monferno",
    searchable_by=["Monferno", "Stage 1", "Monferno"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Mid-air Strike",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)