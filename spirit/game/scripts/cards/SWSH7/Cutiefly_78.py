from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75ab78a4-1504-595b-8688-621e5f7cdff2",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=742,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)