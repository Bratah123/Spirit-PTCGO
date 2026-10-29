from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a9bb3d2c-49fa-5d33-9f1e-ba8a70dc2a76",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosGX.Name",
    display_name="Gyarados-GX",
    searchable_by=["Gyarados-GX", "Stage 1", "GX", "GyaradosGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=16,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Dragon Rage",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Hyper Beam-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=None,
        ),
    ],
)