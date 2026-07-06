from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="134e2f55-e37b-57aa-871f-f80b717864a7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Rapid Strike", "Lopunny"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=213,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Hopping Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)