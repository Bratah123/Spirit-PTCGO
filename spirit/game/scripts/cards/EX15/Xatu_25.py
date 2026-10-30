"""STUB: effect not implemented — do not guess mechanics.
Xatu δ (EX15 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import extra_feather_stage2_ex_boost
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1799c956-eb2a-5d52-973a-3e78ce5f3ca4",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu δ",
    searchable_by=["Xatu \u03b4", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=178,
    abilities=[
        Ability(
            title="Extra Feather",
            game_text="Each of your Stage 2 Pok\u00e9mon-ex does 10 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=extra_feather_stage2_ex_boost(10),
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)