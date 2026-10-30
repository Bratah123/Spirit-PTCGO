"""STUB: effect not implemented — do not guess mechanics.
Lopunny (DP1 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import healing_wish
from spirit.game.card_effects.dp import flop_snipe_switch

card = PokemonCardDef(
    guid="35513487-ed0b-5257-b4a2-5b0ec097bcd6",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Healing Wish",
            game_text="Flip a coin until you get tails. Remove a number of damage counters equal to the number of heads from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=healing_wish(),
        ),
        Attack(
            title="Flop",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) You may switch Lopunny with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flop_snipe_switch(20),
        ),
    ],
)