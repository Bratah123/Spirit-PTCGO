from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b8b3216-0d55-5541-ade4-bd7a6402ae62",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachu.Name",
    display_name="Surfing Pikachu",
    searchable_by=["Surfing Pikachu", "Basic", "SurfingPikachu"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)