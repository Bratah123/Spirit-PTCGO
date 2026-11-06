from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="75af06cd-53b6-5ade-be9b-74e5ef2d8feb",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Bad Dream",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(
                SpecialConditions.ASLEEP, flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,),
            ),
        ),
    ],
)
