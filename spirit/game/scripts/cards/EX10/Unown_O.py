"""STUB: effect not implemented — do not guess mechanics.
Unown (EX10 #O): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import unown_shuffle, unown_shuffle_condition, return_self_and_energy_to_hand

card = PokemonCardDef(
    guid="73147223-87e8-50fd-8a78-bda03d0c5635",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=132,
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
            game_text="Return Unown and all Energy cards attached to it to your hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=return_self_and_energy_to_hand(),
        ),
    ],
)