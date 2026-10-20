"""STUB: effect not implemented — do not guess mechanics.
Gardevoir-EX (XY11 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4fe79a12-be3e-5025-8181-95928bd7ec0a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    display_name="Gardevoir-EX",
    searchable_by=["Gardevoir-EX", "Basic", "EX", "GardevoirEX"],
    subtypes=["Basic", "EX"],
    collector_number=111,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=282,
    abilities=[
        Attack(
            title="Link Blast",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached to them, this attack does 70 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Luminous Blade",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)