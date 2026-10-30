from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_give, unown_give_condition


card = PokemonCardDef(
    guid="ff13f30a-b67b-5e1e-b73f-0117615c86cf",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownG.Name",
    display_name="Unown [G]",
    searchable_by=["Unown [G]", "Basic", "UnownG"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Give]",
            game_text="Once during your turn (before your attack), if you have Unown [G], Unown [I], Unown [V], and Unown [E] on your Bench, you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=unown_give_condition,
            effect=unown_give,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
