"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="43034de5-c3ff-5ac4-98a6-5d7d7f39f76c",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    display_name="Stunky",
    searchable_by=["Stunky", "Basic", "Stunky"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=434,
    abilities=[
        Attack(
            title="Poison Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)