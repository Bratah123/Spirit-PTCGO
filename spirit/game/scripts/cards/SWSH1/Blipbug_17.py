from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82dcba80-d155-5f10-9051-8fefbadaafb6",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    display_name="Blipbug",
    searchable_by=["Blipbug", "Basic", "Blipbug"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)