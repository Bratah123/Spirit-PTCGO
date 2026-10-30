"""STUB: effect not implemented — do not guess mechanics.
Spoink (EX8 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="c52b1161-7874-5624-bf00-a7d11cc1fe14",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    display_name="Spoink",
    searchable_by=["Spoink", "Basic", "Spoink"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=325,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)