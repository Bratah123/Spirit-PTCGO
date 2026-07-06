from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63d04c0f-0dd3-5e59-b07a-2e5e17776b66",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    display_name="Galarian Yamask",
    searchable_by=["Galarian Yamask", "Basic", "GalarianYamask"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=562,
    abilities=[
        Attack(
            title="Brutal Swing",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)