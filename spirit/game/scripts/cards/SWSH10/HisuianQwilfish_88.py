from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b7373e6e-e8f4-528b-b6f3-625aceeeea6d",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianQwilfish.Name",
    display_name="Hisuian Qwilfish",
    searchable_by=["Hisuian Qwilfish", "Basic", "HisuianQwilfish"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=211,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)