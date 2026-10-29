from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0e46aafb-f23b-584b-b71e-a87e8815883f",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PinsirGX.Name",
    display_name="Pinsir-GX",
    searchable_by=["Pinsir-GX", "Basic", "GX", "PinsirGX"],
    subtypes=["Basic", "GX"],
    collector_number=6,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Superpowered Horns",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
        Attack(
            title="Guillotine-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=None,
        ),
    ],
)