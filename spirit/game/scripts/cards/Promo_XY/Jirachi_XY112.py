"""STUB: effect not implemented — do not guess mechanics.
Jirachi (Promo_XY #XY112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="024ef305-0dc3-5374-8913-7d84fb019921",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Precognitive Dream",
            game_text="Draw 3 cards. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)