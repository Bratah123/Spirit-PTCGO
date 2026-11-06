from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_counters_on, flip_damage
from spirit.game.card_effects.ecard import energy_return, energy_return_condition


card = PokemonCardDef(
    guid="3c48063d-9c89-55e6-8191-e3bcf6211ba6",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Energy Return",
            game_text="As often as you like during your turn (before your attack), choose an Energy card attached to 1 of your Pok\u00e9mon and return it to your hand. This power can't be used if Espeon is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=energy_return_condition,
            effect=energy_return,
        ),
        Attack(
            title="Damage Blast",
            game_text="Flip a number of coins equal to the number of damage counters on the Defending Pok\u00e9mon. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(
                coins_from=damage_counters_on("defender"), bonus_per_heads=10),
        ),
    ],
)
