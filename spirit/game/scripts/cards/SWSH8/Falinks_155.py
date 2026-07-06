from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0e159d5-e24e-572d-9034-f9cf52000e6c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Invade",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)