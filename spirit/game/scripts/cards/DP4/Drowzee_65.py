"""DP4 Great Encounters — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1c0ee581-2525-5578-8bec-d5ad85746f20",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="DP4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)