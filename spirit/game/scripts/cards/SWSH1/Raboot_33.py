from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c44d6e73-24e5-5f4f-a027-c801b0dca8dc",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    display_name="Raboot",
    searchable_by=["Raboot", "Stage 1", "Raboot"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
        ),
    ],
)