"""STUB: effect not implemented — do not guess mechanics.
Scizor ex (EX10 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import danger_perception_passive, steel_wing_reduce, cross_cut

card = PokemonCardDef(
    guid="c3426a5c-4be4-511b-aebb-f71b92d452df",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizorex.Name",
    display_name="Scizor ex",
    searchable_by=["Scizor ex", "Stage 1", "ex", "Scizorex"],
    subtypes=["Stage 1", "ex"],
    collector_number=108,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scytherex.Name",
    family_id=212,
    abilities=[
        Ability(
            title="Danger Perception",
            game_text="As long as Scizor ex's remaining HP is 60 or less, Scizor ex does 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=danger_perception_passive(60, 40),
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to Scizor ex by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=steel_wing_reduce(20),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=cross_cut(50, 30),
        ),
    ],
)