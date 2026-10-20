from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15997f31-4c17-5ffd-b650-f0fac9dc87fc",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremEX.Name",
    display_name="White Kyurem-EX",
    searchable_by=["White Kyurem-EX", "Basic", "EX", "WhiteKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=101,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Dragon Stream",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Ice Burn",
            game_text="Discard 2 Fire Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)