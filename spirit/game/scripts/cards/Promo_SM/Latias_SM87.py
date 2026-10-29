from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import diamond_rain
from spirit.game.card_effects.smp import flight_support_passive


card = PokemonCardDef(
    guid="78602eea-0ffe-5207-bd42-408cff16bb51",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Flight Support",
            game_text="Your Latios in play have no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=flight_support_passive,
        ),
        Attack(
            title="Misty Gale",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=diamond_rain,
        ),
    ],
)