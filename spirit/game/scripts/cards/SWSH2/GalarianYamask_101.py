from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2c5e4bd-fc75-520c-abea-d0459d38a32e",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    display_name="Galarian Yamask",
    searchable_by=["Galarian Yamask", "Basic", "GalarianYamask"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=562,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)