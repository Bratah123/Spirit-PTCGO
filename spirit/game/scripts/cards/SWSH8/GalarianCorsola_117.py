from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a15756ff-5af2-57d1-90c7-cce6ae14beae",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    display_name="Galarian Corsola",
    searchable_by=["Galarian Corsola", "Basic", "GalarianCorsola"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=222,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)