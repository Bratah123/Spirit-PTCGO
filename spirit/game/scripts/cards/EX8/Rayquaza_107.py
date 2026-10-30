"""STUB: effect not implemented — do not guess mechanics.
Rayquaza ★ (EX8 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import holy_star_ex_damage, spiral_rush


card = PokemonCardDef(
    guid="5797b371-dd32-57e6-9104-764b157e7eba",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza ★",
    searchable_by=["Rayquaza \u2605", "Basic", "Star", "Rayquaza"],
    subtypes=["Basic", "Star"],
    collector_number=107,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Attack(
            title="Spiral Rush",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=spiral_rush(),
        ),
        Attack(
            title="Holy Star",
            game_text="Discard all Energy cards attached to Rayquaza Star. This attack does 100 damage to each of your opponent's Pok\u00e9mon-ex. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            # STUB: attack effect not implemented
            effect=holy_star_ex_damage(),
        ),
    ],
)