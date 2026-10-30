from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.ex import healing_wind, healing_wind_condition


card = PokemonCardDef(
    guid="06619c6a-10da-593f-9b69-0ffdd64b900b",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Healing Wind",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from each of your Active Pok\u00e9mon. This power can't be used if Xatu is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=healing_wind_condition,
            effect=healing_wind(),
        ),
        Attack(
            title="Psyimpact",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(1, "each_opponent"),
        ),
    ],
)
