from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import mega_drain, no_special_conditions, solar_power


card = PokemonCardDef(
    guid="9386e6db-eb51-5694-8d3c-26100199587d",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=3,
    abilities=[
        Ability(
            title="Solar Power",
            game_text="Once during your turn (before your attack), you may use this power. Your Active Pok\u00e9mon and the Defending Pok\u00e9mon are no longer Asleep, Confused, Paralyzed, or Poisoned. This power can't be used if Venusaur is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=no_special_conditions,
            effect=solar_power,
        ),
        Attack(
            title="Mega Drain",
            game_text="Remove a number of damage counters from Venusaur equal to half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Venusaur has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 4},
            damage=40,
            effect=mega_drain,
        ),
    ],
)
