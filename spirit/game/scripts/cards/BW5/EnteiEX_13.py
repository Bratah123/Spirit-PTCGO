from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f47c607-d366-59ee-9e12-387db779580f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnteiEX.Name",
    display_name="Entei-EX",
    searchable_by=["Entei-EX", "Basic", "EX", "EnteiEX"],
    subtypes=["Basic", "EX"],
    collector_number=13,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Grand Flame",
            game_text="Attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)