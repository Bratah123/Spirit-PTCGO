from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import random_esp


card = PokemonCardDef(
    guid="1b873a8b-5a9e-5b84-b0bf-0f3a9fa33d17",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasPsyduck.Name",
    display_name="Sabrina's Psyduck",
    searchable_by=["Sabrina's Psyduck", "Basic", "SabrinasPsyduck"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Random ESP",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, this attack does no damage and Sabrina's Psyduck is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=random_esp,
        ),
    ],
)
