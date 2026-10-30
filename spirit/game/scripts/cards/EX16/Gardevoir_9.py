from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.ex import (
    has_deck,
    poke_power_condition,
    search_attach_then_counters,
)
from spirit.game.card_effects.trainers import is_psychic_energy_card


card = PokemonCardDef(
    guid="72e1da19-30d9-5654-9bb1-a446e704d2d0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psy Shadow",
            game_text="Once during your turn (before your attack), you may search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. Put 2 damage counters on that Pok\u00e9mon. Shuffle your deck afterward. This power can't be used if Gardevoir is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(has_deck),
            effect=search_attach_then_counters(
                is_psychic_energy_card, counters=2,
                prompt="Choose a Psychic Energy card to attach.",
            ),
        ),
        Attack(
            title="Energy Burst",
            game_text="Does 10 damage times the total amount of Energy attached to Gardevoir and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(
                lambda ctx: count_energy("self")(ctx) + count_energy("defender")(ctx),
                10,
            ),
        ),
    ],
)
