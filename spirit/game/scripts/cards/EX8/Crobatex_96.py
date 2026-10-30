"""STUB: effect not implemented — do not guess mechanics.
Crobat ex (EX8 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import crobat_distortion_counter, cross_attack_flip4, pester_sc_bonus


card = PokemonCardDef(
    guid="6c66ec83-1989-57a9-9f40-266ec2aa8997",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobatex.Name",
    display_name="Crobat ex",
    searchable_by=["Crobat ex", "Stage 2", "ex", "Crobatex"],
    subtypes=["Stage 2", "ex"],
    collector_number=96,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Distortion",
            game_text="Once during your turn (before your attack), if Crobat ex is your Active Pok\u00e9mon, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon. This power can't be used if Crobat ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=crobat_distortion_counter(),
        ),
        Attack(
            title="Cross Attack",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads. If you get 2 or more heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=cross_attack_flip4(),
        ),
        Attack(
            title="Pester",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=pester_sc_bonus(),
        ),
    ],
)