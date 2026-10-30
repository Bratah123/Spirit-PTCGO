"""STUB: effect not implemented — do not guess mechanics.
Tentacool (EX12 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="979d6328-72a8-510e-b472-1d91ea2a6c81",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)