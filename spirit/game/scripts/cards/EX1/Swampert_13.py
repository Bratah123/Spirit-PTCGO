from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import attach_from_hand, poke_power_condition
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_water_energy_card


card = PokemonCardDef(
    guid="da920ce6-4f2f-531b-ab6e-ca41e2f462ad",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Water Call",
            game_text="Once during your turn (before your attack), you may attach a Water Energy card from your hand to your Active Pok\u00e9mon. This power can't be used if Swampert is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(
                requires_hand(is_water_energy_card, exclude_self=False)),
            effect=attach_from_hand(
                is_water_energy_card, target="active",
                prompt="Choose a Water Energy card to attach.",
            ),
        ),
        Attack(
            title="Hypno Splash",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
