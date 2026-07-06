from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0be748d9-42d7-51c6-81aa-9daefb441bc2",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic", "Starly"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=396,
    abilities=[
        Ability(
            title="Sky Circus",
            game_text="If you played Bird Keeper from your hand during this turn, ignore all Energy in this Pok\u00e9mon's attack costs.",
            effect=unimplemented,
        ),
        Attack(
            title="Keen Eye",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)