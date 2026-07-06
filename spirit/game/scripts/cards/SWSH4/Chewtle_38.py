from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3099d0be-88fe-5beb-bcb8-fa8ef0ed401c",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    display_name="Chewtle",
    searchable_by=["Chewtle", "Basic", "Chewtle"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=833,
    abilities=[
        Attack(
            title="Jaw Lock",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)