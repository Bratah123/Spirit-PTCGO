from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96dc52bf-33b7-5439-b011-75f65f9bbd67",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachuV.Name",
    display_name="Surfing Pikachu V",
    searchable_by=["Surfing Pikachu V", "Basic", "V", "SurfingPikachuV"],
    subtypes=["Basic", "V"],
    collector_number=8,
    set_code="CEL25",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3},
            damage=150,
        ),
    ],
)