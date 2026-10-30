"""STUB: effect not implemented — do not guess mechanics.
Lumineon (DP7 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp5_combee_59_flitter


card = PokemonCardDef(
    guid="c7bcf659-e5ee-577d-a136-a0b01dc1bc55",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name",
    display_name="Lumineon",
    searchable_by=["Lumineon", "Stage 1", "Lumineon"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    family_id=456,
    abilities=[
        Ability(
            title="Fin Luster",
            game_text="Once during your turn (before your attack), if Lumineon is your Active Pok\u00e9mon, you may look at your opponent's hand. If your opponent's Bench isn't full, choose 1 Basic Pok\u00e9mon from your opponent's hand, and put it onto his or her Bench. Then, switch it with the Defending Pok\u00e9mon. This power can't be used if Lumineon is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Quick Swim",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={},
            # STUB: attack effect not implemented
            effect=dp5_combee_59_flitter(),
        ),
        Attack(
            title="Elegant Swim",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Lumineon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)