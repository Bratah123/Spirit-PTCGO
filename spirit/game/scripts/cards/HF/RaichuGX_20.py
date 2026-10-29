from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f455dedf-143a-5c68-9ee0-a39228e0fa8a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuGX.Name",
    display_name="Raichu-GX",
    searchable_by=["Raichu-GX", "Stage 1", "GX", "RaichuGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=20,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Thunderbolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Spark Ball-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=None,
        ),
    ],
)