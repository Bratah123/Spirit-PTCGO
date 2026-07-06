from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95ee77dc-dd7e-56af-b800-bcd502432ae7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name",
    display_name="Pyukumuku",
    searchable_by=["Pyukumuku", "Basic", "Pyukumuku"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=771,
    abilities=[
        Ability(
            title="Pitch a Pyukumuku",
            game_text="Once during your turn, if this Pok\u00e9mon is in your hand, you may reveal it and put it on the bottom of your deck. If you do, draw a card. You can't use more than 1 Pitch a Pyukumuku Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)