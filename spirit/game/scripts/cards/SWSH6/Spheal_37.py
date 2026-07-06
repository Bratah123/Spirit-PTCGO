from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="342fb37b-5072-5490-a0a2-bbb10d64fd30",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    display_name="Spheal",
    searchable_by=["Spheal", "Basic", "Spheal"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)