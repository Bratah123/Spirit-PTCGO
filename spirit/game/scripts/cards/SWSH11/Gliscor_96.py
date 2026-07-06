from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6299830c-db10-5d94-b580-5c13937f4793",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Hurricane Shock",
            game_text="Flip 4 coins. This attack does 50 damage for each heads. If at least 2 of them are heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)