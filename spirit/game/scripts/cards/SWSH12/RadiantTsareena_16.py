from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ce58ea2-6f3f-5f2d-abc9-326bb72fefa7",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantTsareena.Name",
    display_name="Radiant Tsareena",
    searchable_by=["Radiant Tsareena", "Basic", "Radiant", "RadiantTsareena"],
    subtypes=["Basic", "Radiant"],
    collector_number=16,
    set_code="SWSH12",
    rarity=Rarities.RareRadiant,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=763,
    abilities=[
        Ability(
            title="Elegant Heal",
            game_text="Once during your turn, you may heal 20 damage from each of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aroma Shot",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)