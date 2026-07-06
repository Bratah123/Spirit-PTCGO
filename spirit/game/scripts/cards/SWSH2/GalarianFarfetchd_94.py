from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c5b7618-c545-5d1f-ac72-168753905545",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name",
    display_name="Galarian Farfetch'd",
    searchable_by=["Galarian Farfetch'd", "Basic", "GalarianFarfetchd"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=83,
    abilities=[
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)