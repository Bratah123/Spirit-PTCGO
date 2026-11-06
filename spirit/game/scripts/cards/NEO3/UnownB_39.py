from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_bear, unown_bear_condition


card = PokemonCardDef(
    guid="a4387294-7cc1-5974-ae25-facd4e921ec0",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownB.Name",
    display_name="Unown [B]",
    searchable_by=["Unown [B]", "Basic", "UnownB"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Bear]",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon with Unown in its name to Unown [B]. This power can't be used if Unown [B] has 10 HP left. This power can be used even if Unown [B] is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=unown_bear_condition,
            effect=unown_bear,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
