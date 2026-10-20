from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0746b827-e893-5ff8-a6b6-c597bfdb8e87",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    display_name="Team Aqua's Spheal",
    searchable_by=["Team Aqua's Spheal", "Basic", "TeamAquasSpheal"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)