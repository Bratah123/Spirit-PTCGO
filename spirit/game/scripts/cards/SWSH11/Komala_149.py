from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aaac1bf0-77c7-5481-b9e9-356d2a7f0ea5",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic", "Komala"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="All Just a Dream",
            game_text="If this Pok\u00e9mon is Asleep and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, your opponent can't take any Prize cards for it.",
            effect=unimplemented,
        ),
        Attack(
            title="Collapse",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)