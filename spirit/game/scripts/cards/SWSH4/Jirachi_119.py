from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="920411e1-3b6e-5bc9-89db-966fe258f489",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Dreamy Revelation",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card back on top of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Amazing Star",
            game_text="Search your deck for up to 7 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
    ],
)