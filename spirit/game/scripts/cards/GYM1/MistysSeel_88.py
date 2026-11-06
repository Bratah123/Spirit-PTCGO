from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46fdbcd0-b04a-5dbc-84fb-8779a8a4532f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeel.Name",
    display_name="Misty's Seel",
    searchable_by=["Misty's Seel", "Basic", "MistysSeel"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)