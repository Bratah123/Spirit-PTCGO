"""STUB: effect not implemented — do not guess mechanics.
Unown (EX10 #R): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import scoop_defending_to_hand, unown_shuffle, unown_shuffle_condition


card = PokemonCardDef(
    guid="fa84eef8-4338-530a-9995-7e6738b83a9c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=135,
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
            game_text="Flip a coin. If heads, your opponent returns the Defending Pok\u00e9mon and all cards attached to it to his or her hand. (If your opponent doesn't have any Benched Pok\u00e9mon or other Active Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=scoop_defending_to_hand(flip=True),
        ),
    ],
)