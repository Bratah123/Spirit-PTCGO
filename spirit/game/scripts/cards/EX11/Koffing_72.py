"""STUB: effect not implemented — do not guess mechanics.
Koffing (EX11 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7e238448-8b15-5977-b7d2-17c118c84a94",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Confusion Gas",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)