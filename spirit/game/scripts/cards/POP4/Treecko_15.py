"""STUB: effect not implemented — do not guess mechanics.
Treecko δ (EX14 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="40188e36-03da-5dc9-b6ba-d5efe4ec3e1d",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko δ",
    searchable_by=["Treecko \u03b4", "Basic", "Treecko"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="POP4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=252,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Shining Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)