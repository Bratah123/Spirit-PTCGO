from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="546c3705-a69d-584b-bae7-b1faaabecea4",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    display_name="Morelull",
    searchable_by=["Morelull", "Basic", "Morelull"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=755,
    abilities=[
        Attack(
            title="Spore",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)