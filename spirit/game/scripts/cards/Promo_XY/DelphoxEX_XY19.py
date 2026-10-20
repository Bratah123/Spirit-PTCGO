"""STUB: effect not implemented — do not guess mechanics.
Delphox-EX (Promo_XY #XY19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd1814d1-80df-579c-bdb8-ec6a06e6649a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxEX.Name",
    display_name="Delphox-EX",
    searchable_by=["Delphox-EX", "Basic", "EX", "DelphoxEX"],
    subtypes=["Basic", "EX"],
    collector_number=19,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=655,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wonder Flare",
            game_text="Your opponent reveals his or her hand. This attack does 40 more damage for each Energy card in your opponent's hand.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)