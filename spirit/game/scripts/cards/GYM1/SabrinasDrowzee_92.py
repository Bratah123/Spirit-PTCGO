from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import suggestion


card = PokemonCardDef(
    guid="411e8871-3016-5191-a93f-69ed9b7c8bac",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasDrowzee.Name",
    display_name="Sabrina's Drowzee",
    searchable_by=["Sabrina's Drowzee", "Basic", "SabrinasDrowzee"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Suggestion",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=suggestion,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
