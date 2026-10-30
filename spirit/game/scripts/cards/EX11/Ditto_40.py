"""STUB: effect not implemented — do not guess mechanics.
Ditto (EX11 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import ditto_duplicate, ditto_duplicate_condition, poke_power_condition, smash_turn
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="f1fa034c-3a7f-5b7f-bf08-128bd276c91a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
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
            title="Smash Turn",
            game_text="After your attack, you may switch Ditto with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=smash_turn(),
        ),
    ],
)