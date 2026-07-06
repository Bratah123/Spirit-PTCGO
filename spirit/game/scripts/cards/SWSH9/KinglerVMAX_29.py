from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81c73b9b-e186-5cd0-90fa-75dabdf97620",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KinglerVMAX.Name",
    display_name="Kingler VMAX",
    searchable_by=["Kingler VMAX", "VMAX", "KinglerVMAX"],
    subtypes=["VMAX"],
    collector_number=29,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KinglerV.Name",
    family_id=99,
    abilities=[
        Attack(
            title="Bubbles Galore",
            game_text="Search your deck for up to 5 Water Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Pincer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)