from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c87f1933-fe89-5281-9934-bba765c24275",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    display_name="Carkol",
    searchable_by=["Carkol", "Stage 1", "Carkol"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)