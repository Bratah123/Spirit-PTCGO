"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Groudon (EX4 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import power_saver_condition, second_strike


card = PokemonCardDef(
    guid="097d53da-0083-54ac-a6ea-81773a20bb3c",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasGroudon.Name",
    display_name="Team Magma's Groudon",
    searchable_by=["Team Magma's Groudon", "Basic", "TeamMagmasGroudon"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="As long as the number of Pok\u00e9mon in play (both yours and your opponent's) that has Team Magma in its name is 3 or less, Team Magma's Groudon can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=None,
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            condition=power_saver_condition("Team Magma"),
            effect=snipe_attack(20, pool='any', count=1),
        ),
        Attack(
            title="Pulverize",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            condition=power_saver_condition("Team Magma"),
            effect=second_strike(50, 20, 2),
        ),
    ],
)