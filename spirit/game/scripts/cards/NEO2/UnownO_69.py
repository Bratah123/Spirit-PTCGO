from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_observe, unown_observe_condition


card = PokemonCardDef(
    guid="175cae85-4c9c-510d-9e5c-951624feb3f7",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownO.Name",
    display_name="Unown [O]",
    searchable_by=["Unown [O]", "Basic", "UnownO"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Observe]",
            game_text="Once during your turn (before your attack), you may look at 5 cards from the top of your opponent's deck and put them back in the same order.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=unown_observe_condition,
            effect=unown_observe,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
