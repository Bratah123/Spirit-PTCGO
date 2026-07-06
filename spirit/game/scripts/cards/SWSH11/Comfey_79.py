from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import flower_selecting, in_active_spot

card = PokemonCardDef(
    guid="1da5ad81-7a21-5fc3-a3e7-55d2f397ca70",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Ability(
            title="Flower Selecting",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card in the Lost Zone.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=flower_selecting,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
