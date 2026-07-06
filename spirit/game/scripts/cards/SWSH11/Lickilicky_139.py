from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b4ba2074-5d37-59ef-b22b-11fd9ec15090",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Tongue Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
        ),
    ],
)