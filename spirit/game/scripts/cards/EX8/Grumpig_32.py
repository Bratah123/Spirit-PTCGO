"""STUB: effect not implemented — do not guess mechanics.
Grumpig (EX8 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import mega_throw, self_control_immune


card = PokemonCardDef(
    guid="16947069-fa32-5dc5-b822-cd35f508ed2e",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name",
    display_name="Grumpig",
    searchable_by=["Grumpig", "Stage 1", "Grumpig"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    family_id=325,
    abilities=[
        Ability(
            title="Carefree",
            game_text="Grumpig can't be Confused.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=self_control_immune(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Hypnoblast",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Extra Ball",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=mega_throw(50, 30),
        ),
    ],
)