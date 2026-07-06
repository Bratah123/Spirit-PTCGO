from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1cb2538-a51f-5c40-a17a-0897447647a0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosVMAX.Name",
    display_name="Gyarados VMAX",
    searchable_by=["Gyarados VMAX", "VMAX", "GyaradosVMAX"],
    subtypes=["VMAX"],
    collector_number=207,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosV.Name",
    family_id=130,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Max Tyrant",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)