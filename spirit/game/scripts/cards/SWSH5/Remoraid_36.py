from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30f68f18-a264-596b-b8ff-961418d30f9a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic", "Rapid Strike", "Remoraid"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=36,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Fin",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)