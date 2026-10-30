"""STUB: effect not implemented — do not guess mechanics.
Unown (EX10 #F): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import unown_shuffle, unown_shuffle_condition, flip3_conditions_asleep_paralyze_confuse

card = PokemonCardDef(
    guid="6b4b879e-cd84-5f44-9903-698fd43ac8a1",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="Shuffle",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Shuffle",
            condition=unown_shuffle_condition(),
            game_text="Once during your turn (before your attack), you may search your deck for another Unown and switch it with Unown. (Any cards attached to Unown, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Unown on top of your deck. Shuffle your deck afterward. You can't use more than 1 Shuffle Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=unown_shuffle(),
        ),
        Attack(
            title="Hidden Power",
            game_text="Flip 3 coins. If 1 of them is heads, the Defending Pok\u00e9mon is now Asleep. If 2 of them are heads, the Defending Pok\u00e9mon is now Confused. If all of them are heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip3_conditions_asleep_paralyze_confuse(),
        ),
    ],
)