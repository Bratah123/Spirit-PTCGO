from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f4e0a55-4e26-59f3-a33a-27bd8d5c50e1",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    display_name="Pikipek",
    searchable_by=["Pikipek", "Basic", "Pikipek"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=731,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)