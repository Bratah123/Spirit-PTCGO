"""STUB: effect not implemented — do not guess mechanics.
Electivire (DP1 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import giga_impact_may_discard
from spirit.game.card_effects.dp import intense_voltage, intense_voltage_condition, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="5214707c-7c51-55c8-8c4b-ef0fe61cbea1",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Ability(
            title="Intense Voltage",
            game_text="As often as you like during your turn (before your attack), if Elekid is anywhere under Electivire, you may move a Lightning Energy attached to your Pok\u00e9mon to Electivire. This power can't be used if Electivire is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(intense_voltage_condition),
            activation=Activations.UNLIMITED,
            effect=intense_voltage(),
        ),
        Attack(
            title="Giga Impact",
            game_text="You may discard all Lightning Energy attached to Electivire. If you do, this attack's base damage is 120 instead of 60.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=giga_impact_may_discard(),
        ),
    ],
)