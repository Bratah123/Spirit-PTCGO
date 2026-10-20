"""STUB: effect not implemented — do not guess mechanics.
Metagross-EX (Promo_XY #XY34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b36186e-dd0c-5fe5-839e-9dcc6f5ed0ba",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossEX.Name",
    display_name="Metagross-EX",
    searchable_by=["Metagross-EX", "Basic", "EX", "MetagrossEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=376,
    abilities=[
        Attack(
            title="Magnetic Laser",
            game_text="You may move a Metal Energy from 1 of your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Squared Attack",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)