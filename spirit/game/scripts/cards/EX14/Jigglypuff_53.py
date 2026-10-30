"""STUB: effect not implemented — do not guess mechanics.
Jigglypuff (EX14 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="5410b96e-af8b-5377-a68e-b61b25ebe6a8",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=39,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)