"""STUB: effect not implemented — do not guess mechanics.
Snorlax δ (EX15 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import bedhead_asleep_between_turns, dozing_heal_and_asleep
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e02e9b67-fa5b-52df-a557-eb6c70d13cad",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax δ",
    searchable_by=["Snorlax \u03b4", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Bedhead",
            game_text="As long as Snorlax remains Asleep between turns, put 2 damage counters on 1 of the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=bedhead_asleep_between_turns(2),
        ),
        Ability(
            title="Dozing",
            game_text="Once during your turn (before your attack), if Snorlax is your Active Pok\u00e9mon, you may remove 2 damage counters from Snorlax and Snorlax is now Asleep. This power can't be used if Snorlax is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=dozing_heal_and_asleep(2),
        ),
    ],
)