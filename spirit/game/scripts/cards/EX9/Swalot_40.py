"""STUB: effect not implemented — do not guess mechanics.
Swalot (EX9 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.card_effects.ex import blot_heal
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1ce00e9b-8e26-5fd8-b3ab-49e20ea25cb6",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1", "Swalot"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Blot",
            game_text="Remove 1 damage counter from Swalot.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=blot_heal(1),
        ),
        Attack(
            title="Poison Breath",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)