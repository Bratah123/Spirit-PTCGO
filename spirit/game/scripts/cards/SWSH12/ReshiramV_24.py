from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7d6acfc-61c0-50e0-b7f6-8a9438848df6",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramV.Name",
    display_name="Reshiram V",
    searchable_by=["Reshiram V", "Basic", "V", "ReshiramV"],
    subtypes=["Basic", "V"],
    collector_number=24,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Sparkling Wing",
            game_text="Search your deck for up to 2 basic Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="White Blaze",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)