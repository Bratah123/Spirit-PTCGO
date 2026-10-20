from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77897f6d-07b4-5660-b730-1c70223b84e6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=299,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)