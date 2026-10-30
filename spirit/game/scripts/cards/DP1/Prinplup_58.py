"""STUB: effect not implemented — do not guess mechanics.
Prinplup (DP1 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import breaking_sound
from spirit.game.card_effects.dp import brine


card = PokemonCardDef(
    guid="08be9ef2-88c1-5474-9916-b083b5d06720",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1", "Prinplup"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Aqua Shower",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=breaking_sound(10),
        ),
        Attack(
            title="Brine",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any damage counters on it. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2},
            effect=brine(40),
        ),
    ],
)