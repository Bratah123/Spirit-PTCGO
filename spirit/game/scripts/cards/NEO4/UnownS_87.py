from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_search, unown_search_condition


card = PokemonCardDef(
    guid="e0e5afcf-ef68-5d86-85c6-46bba2f2c9ca",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownS.Name",
    display_name="Unown [S]",
    searchable_by=["Unown [S]", "Basic", "UnownS"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Search]",
            game_text="Once during your turn (before your attack), you may look at 1 of your Prize cards. Return that Prize card face down. This power can be used even if Unown [S] is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=unown_search_condition,
            effect=unown_search,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
