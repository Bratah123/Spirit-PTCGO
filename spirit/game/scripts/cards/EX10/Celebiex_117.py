"""STUB: effect not implemented — do not guess mechanics.
Celebi ex (EX10 #117): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiral_leaf, time_trap

card = PokemonCardDef(
    guid="8b25329c-0668-5742-95b7-89eb26586a76",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebiex.Name",
    display_name="Celebi ex",
    searchable_by=["Celebi ex", "Basic", "ex", "Celebiex"],
    subtypes=["Basic", "ex"],
    collector_number=117,
    set_code="EX10",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Spiral Leaf",
            game_text="Flip a coin. If heads, put 1 damage counter on each of your opponent's Pok\u00e9mon. If tails, remove 1 damage counter from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=spiral_leaf(),
        ),
        Attack(
            title="Time Trap",
            game_text="Flip a coin. If heads, look at the top 4 cards of your opponent's deck, and put them back on top of your opponent's deck in any order. If tails, look at the top 4 cards of your deck, and put them back on top of your deck in any order.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=time_trap(4),
        ),
    ],
)