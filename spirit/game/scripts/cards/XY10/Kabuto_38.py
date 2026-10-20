from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="000ce88b-2da3-5fda-a797-1af27368fd2c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Restored", "Kabuto"],
    subtypes=["Restored"],
    collector_number=38,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DomeFossilKabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)