from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87998471-a3d2-55bd-84e2-b3922e2c8e6c",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic", "Single Strike", "Shuppet"],
    subtypes=["Basic", "Single Strike"],
    collector_number=62,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=353,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)