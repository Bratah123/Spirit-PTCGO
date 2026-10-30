"""STUB: effect not implemented — do not guess mechanics.
Ditto (EX11 #61): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import ditto_duplicate, ditto_duplicate_condition, fireworks_discard_fire, poke_power_condition
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a09e3a7c-b658-5450-b92b-7bc51e0fe0c7",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=132,
    abilities=[
        Ability(
            title="Duplicate",
            game_text="Once during your turn (before your attack), you may search your deck for another Ditto and switch it with Ditto. (Any cards attached to Ditto, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Ditto on top of your deck. Shuffle your deck afterward. You can't use more than 1 Duplicate Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Duplicate",
            condition=ditto_duplicate_condition(),
            effect=ditto_duplicate(),
        ),
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Ditto.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=fireworks_discard_fire(),
        ),
    ],
)