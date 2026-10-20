from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6206133e-47b0-5ff7-b308-67bf08764091",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremEX.Name",
    display_name="Black Kyurem-EX",
    searchable_by=["Black Kyurem-EX", "Basic", "EX", "BlackKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=145,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Dragon Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Freeze Shock",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)