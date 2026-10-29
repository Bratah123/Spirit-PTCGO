"""STUB: effect not implemented — do not guess mechanics.
Raichu-GX (SL #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    condition_attack, count_energy, damage_per, recoil_attack,
)
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="dd3c57fe-b277-5671-8673-41efcab3759e",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuGX.Name",
    display_name="Raichu-GX",
    searchable_by=["Raichu-GX", "Stage 1", "GX", "RaichuGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=29,
    set_code="SL",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Powerful Spark",
            game_text="This attack does 20 more damage times the amount of Lightning Energy attached to your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("mine", PokemonTypes.LIGHTNING), 20, base=20),
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=recoil_attack(30),
        ),
        Attack(
            title="Voltail-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
    ],
)