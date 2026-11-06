from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ed31315a-6692-5053-80c1-c1c05031641f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasWeedle.Name",
    display_name="Koga's Weedle",
    searchable_by=["Koga's Weedle", "Basic", "KogasWeedle"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Sting",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Stinger",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned; if tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.PARALYZED,),
            ),
        ),
    ],
)
