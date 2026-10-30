"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Sharpedo (EX4 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, cant_attack_next_turn

card = PokemonCardDef(
    guid="f5b6b1c4-57f7-55c4-b68b-f4cfa4178cad",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSharpedo.Name",
    display_name="Team Aqua's Sharpedo",
    searchable_by=["Team Aqua's Sharpedo", "Stage 1", "TeamAquasSharpedo"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Team Aqua's Sharpedo.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(damage_counters_on("self"), 10, base=10),
        ),
        Attack(
            title="Aqua Slash",
            game_text="Team Aqua's Sharpedo can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=cant_attack_next_turn(),
        ),
    ],
)