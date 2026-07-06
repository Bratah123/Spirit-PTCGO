from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe1c3af4-e99a-5407-b5b7-098f66828cb2",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianVoltorb.Name",
    display_name="Hisuian Voltorb",
    searchable_by=["Hisuian Voltorb", "Basic", "HisuianVoltorb"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=100,
    abilities=[
        Attack(
            title="Cheerful Charge",
            game_text="You can use this attack only if you go second, and only during your first turn. Choose up to 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a basic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)