from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6fac54f-cf7e-5868-a5cb-b8763db7f667",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachu.Name",
    display_name="Surfing Pikachu",
    searchable_by=["Surfing Pikachu", "Basic", "SurfingPikachu"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
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