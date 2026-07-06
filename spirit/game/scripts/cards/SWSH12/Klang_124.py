from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f061ff4-5307-53f7-abdd-ec1e129962b8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    display_name="Klang",
    searchable_by=["Klang", "Stage 1", "Klang"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Gear Grind",
            game_text="Flip 2 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)