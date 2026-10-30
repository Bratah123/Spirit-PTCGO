"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Sharpedo (EX4 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import bonus_if_special_condition, delayed_condition

card = PokemonCardDef(
    guid="feb97d5f-70fa-5dbb-914f-e1bdc0a60eae",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSharpedo.Name",
    display_name="Team Aqua's Sharpedo",
    searchable_by=["Team Aqua's Sharpedo", "Stage 1", "TeamAquasSharpedo"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Slow-Acting Poison",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=delayed_condition(SpecialConditions.POISONED),
        ),
        Attack(
            title="Aqua Smash",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_special_condition(20),
        ),
    ],
)