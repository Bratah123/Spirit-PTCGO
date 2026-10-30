"""STUB: effect not implemented — do not guess mechanics.
Camerupt (EX9 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.card_effects.ex import bonus_if_ex
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7b03c258-4325-5da8-99bb-2a372dd05c3b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1", "Camerupt"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Extra Flame",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_ex(30),
        ),
        Attack(
            title="Super Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)