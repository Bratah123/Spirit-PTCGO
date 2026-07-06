from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e118592-fd9a-5428-8434-5b480f7c206a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish", "Basic", "Frillish"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=592,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy from this Pok\u00e9mon and heal all damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)