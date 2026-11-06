from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import (
    all_conditions, has_cards_in_deck, no_special_conditions, special_delivery,
)


card = PokemonCardDef(
    guid="44d15e04-fb45-5b0c-9840-5006c213b88b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Ability(
            title="Special Delivery",
            game_text="Once during your turn (before your attack), you may draw a card. If you do, choose a card from your hand and put it on top of your deck. This power can't be used if Dragonite is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=all_conditions(no_special_conditions, has_cards_in_deck),
            effect=special_delivery,
        ),
        Attack(
            title="Supersonic Flight",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)
