from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62b1d1a7-a160-503d-9af8-8198033f51ea",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    display_name="Skitty",
    searchable_by=["Skitty", "Basic", "Skitty"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=300,
    abilities=[
        Attack(
            title="Drawup Power",
            game_text="Search your deck for an Energy card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cat Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)