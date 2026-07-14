from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="815e5788-0ccd-5b26-8646-77eb47fb6e9f",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewV.Name",
    display_name="Mew V",
    searchable_by=["Mew V", "Basic", "V", "Fusion Strike", "MewV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=60,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Attack(
            title="Energy Mix",
            game_text="Search your deck for an Energy card and attach it to 1 of your Fusion Strike Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Leap",
            game_text="You may shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)