"""STUB: effect not implemented — do not guess mechanics.
Dusclops (DP1 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import roam_counters
from spirit.game.card_effects.dp import gravity_wave

card = PokemonCardDef(
    guid="e021dfa4-6073-5219-91ff-30572e769714",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    display_name="Dusclops",
    searchable_by=["Dusclops", "Stage 1", "Dusclops"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Attack(
            title="Roam",
            game_text="Flip a coin. If heads, put 2 damage counters on each of your opponent's Pok\u00e9mon. If tails, put 2 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=roam_counters(2),
        ),
        Attack(
            title="Gravity Wave",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that doesn't have a Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=gravity_wave(10),
        ),
    ],
)