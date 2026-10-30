"""STUB: effect not implemented — do not guess mechanics.
Vibrava δ (EX15 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import conditions_if
from spirit.game.card_effects.ex import defender_is_ex


card = PokemonCardDef(
    guid="b751068b-3c34-5d09-8f9d-549f1a4c6db0",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava δ",
    searchable_by=["Vibrava \u03b4", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=329,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Sonic Noise",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, that Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_is_ex, SpecialConditions.CONFUSED),
        ),
    ],
)