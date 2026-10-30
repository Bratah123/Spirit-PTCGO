"""STUB: effect not implemented — do not guess mechanics.
Vespiquen (DP1 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import leaf_honey
from spirit.game.card_effects.dp import attack_order

card = PokemonCardDef(
    guid="7bda3eb5-f731-5b51-9f31-ba94ed507694",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Leaf Honey",
            game_text="Discard a Grass Energy attached to Vespiquen and remove all damage counters from 1 of your Benched Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=leaf_honey(),
        ),
        Attack(
            title="Attack Order",
            game_text="Does 10 damage times the number of Grass Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=attack_order(),
        ),
    ],
)