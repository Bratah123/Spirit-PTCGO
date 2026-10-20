from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60cbb51d-9978-56dc-99ca-48cc1b1d1610",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    display_name="Amaura",
    searchable_by=["Amaura", "Restored", "Amaura"],
    subtypes=["Restored"],
    collector_number=25,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SailFossil.Name",
    family_id=698,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)