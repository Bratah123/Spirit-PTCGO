from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7db5980-9cc5-5f90-b89d-b0ece3ac736b",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    display_name="Rolycoly",
    searchable_by=["Rolycoly", "Basic", "Rolycoly"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=837,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)