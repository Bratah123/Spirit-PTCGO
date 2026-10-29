from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.smp import power_suction, power_suction_condition, psycho_boost

card = PokemonCardDef(
    guid="c8af6223-78de-5f42-82c1-94e23bad39da",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Power Suction",
            game_text="Once during your turn (before your attack), you may move an Energy from 1 of your Pok\u00e9mon to 1 of your Deoxys.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=power_suction,
            activation=Activations.ONCE_PER_TURN,
            condition=power_suction_condition,
        ),
        Attack(
            title="Psycho Boost",
            game_text="During your next turn, this Pok\u00e9mon's Psycho Boost attack's base damage is 50.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=psycho_boost,
        ),
    ],
)