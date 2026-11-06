from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import (
    all_conditions,
    boost_named_attack_this_turn,
    no_special_conditions,
    remaining_hp_at_most,
)


card = PokemonCardDef(
    guid="ce818687-03ce-5889-8f94-1b6766405465",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Ability(
            title="Final Blow",
            game_text="If Heracross's remaining HP are 20 or less, you may make its Megahorn attack's base damage 120 instead of 60. This power can't be used if Heracross is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=all_conditions(no_special_conditions, remaining_hp_at_most(20)),
            effect=boost_named_attack_this_turn("Megahorn", 60),
        ),
        Attack(
            title="Megahorn",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 3},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)
