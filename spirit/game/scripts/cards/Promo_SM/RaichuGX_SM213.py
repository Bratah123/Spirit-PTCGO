from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9d03f92-fa5f-5966-8e14-de101270a511",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuGX.Name",
    display_name="Raichu-GX",
    searchable_by=["Raichu-GX", "Stage 1", "GX", "RaichuGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=213,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
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