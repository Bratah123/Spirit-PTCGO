"""STUB: effect not implemented — do not guess mechanics.
Shiftry (EX8 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import fan_action_switch, stadium_power_bonus


card = PokemonCardDef(
    guid="11d5d26b-f509-5dc5-8d06-b176e4837969",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Fan Action",
            game_text="Once during your turn (before your attack), you may switch 1 of the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. Your opponent chooses the Benched Pok\u00e9mon to switch. This power can't be used if Shiftry is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=fan_action_switch(),
        ),
        Attack(
            title="Stadium Power",
            game_text="If there is any Stadium card in play, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=stadium_power_bonus(),
        ),
    ],
)