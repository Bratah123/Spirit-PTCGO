"""STUB: effect not implemented — do not guess mechanics.
Seaking (EX8 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import rend_if_damaged, triple_breach


card = PokemonCardDef(
    guid="0d985a68-3e7e-5958-9c11-4813f41f19f9",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name",
    display_name="Seaking",
    searchable_by=["Seaking", "Stage 1", "Seaking"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Triple Breach",
            game_text="Choose 3 of your opponent's Pok\u00e9mon. This attack does 10 damage to each of those Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=triple_breach(),
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=rend_if_damaged(),
        ),
    ],
)