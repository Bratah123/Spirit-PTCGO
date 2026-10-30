from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import trickery, trickery_condition


card = PokemonCardDef(
    guid="edfc7846-65f2-53b4-a48f-ba6ff75e5439",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=19,
    abilities=[
        Ability(
            title="Trickery",
            game_text="Once during your turn (before your attack), you may switch 1 of your Prizes with the top card of your deck. This power can't be used if Rattata is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=trickery_condition,
            effect=trickery,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
