"""STUB: effect not implemented — do not guess mechanics.
Giratina-EX (XY7 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8197583-3043-5321-aa31-0ff38776c77d",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaEX.Name",
    display_name="Giratina-EX",
    searchable_by=["Giratina-EX", "Basic", "EX", "GiratinaEX"],
    subtypes=["Basic", "EX"],
    collector_number=93,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=487,
    abilities=[
        Ability(
            title="Renegade Pulse",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Mega Evolution Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Chaos Wheel",
            game_text="Your opponent can't play any Pok\u00e9mon Tool, Special Energy, or Stadium cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)