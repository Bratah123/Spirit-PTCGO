"""STUB: effect not implemented — do not guess mechanics.
Ash-Greninja-EX (Promo_XY #XY133): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d76a55a-dd34-5d5a-9b85-f6860b1a9bbf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AshGreninjaEX.Name",
    display_name="Ash-Greninja-EX",
    searchable_by=["Ash-Greninja-EX", "Basic", "EX", "AshGreninjaEX"],
    subtypes=["Basic", "EX"],
    collector_number=133,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=658,
    abilities=[
        Attack(
            title="Dancing Shuriken",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ninja Blade",
            game_text="This Pok\u00e9mon can't use Ninja Blade during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)