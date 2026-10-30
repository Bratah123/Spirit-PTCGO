"""STUB: effect not implemented — do not guess mechanics.
Gyarados (EX8 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.ex import full_retaliation_magikarp, pulverize_if_damaged



card = PokemonCardDef(
    guid="c41dcff2-60a6-5e27-b768-c709bef767e0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Dragon Spark",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Full Retaliation",
            game_text="Does 20 damage times the number of damage counters on all of your Magikarp.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=full_retaliation_magikarp(),
        ),
        Attack(
            title="Pulverize",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=pulverize_if_damaged(),
        ),
    ],
)