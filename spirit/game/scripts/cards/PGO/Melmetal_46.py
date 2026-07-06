from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1eb170c9-255f-5716-af07-873244bb18c4",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Melmetal"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Swinging Smash",
            game_text="Flip 2 coins. This attack does 90 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)