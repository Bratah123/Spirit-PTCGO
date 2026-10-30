from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.ex import delayed_condition

card = PokemonCardDef(
    guid="b1546668-af51-578d-b78b-c1a92196970b",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Slow Trip Gas",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=delayed_condition(SpecialConditions.CONFUSED),
        ),
    ],
)