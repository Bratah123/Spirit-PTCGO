"""STUB: effect not implemented — do not guess mechanics.
Swellow (EX3 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import quick_dive


card = PokemonCardDef(
    guid="aae1bc07-c906-5cf0-9968-205c8861ad27",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Quick Dive",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 50 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=quick_dive(50),
        ),
    ],
)