"""STUB: effect not implemented — do not guess mechanics.
Absol ex (EX16 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import clay_pulse, cursed_eyes_move_counters


card = PokemonCardDef(
    guid="3fb22146-df1f-5afe-88ae-5b52135bd57c",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absolex.Name",
    display_name="Absol ex",
    searchable_by=["Absol ex", "Basic", "ex", "Absolex"],
    subtypes=["Basic", "ex"],
    collector_number=92,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Ability(
            title="Cursed Eyes",
            game_text="Once during your turn, when you put Absol ex from your hand onto your Bench, you may move 3 damage counters from 1 of your opponent's Pok\u00e9mon to another of his or her Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=cursed_eyes_move_counters(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Psychic Pulse",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=clay_pulse(),
        ),
    ],
)