"""STUB: effect not implemented — do not guess mechanics.
Sharpedo-EX (XY5 #152): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="413be683-827b-52e1-8626-124a1eef5f58",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name",
    display_name="Sharpedo-EX",
    searchable_by=["Sharpedo-EX", "Basic", "EX", "SharpedoEX"],
    subtypes=["Basic", "EX"],
    collector_number=152,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=319,
    abilities=[
        Attack(
            title="Hunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jagged Fang",
            game_text="Discard an Energy attached to this Pok\u00e9mon. Then, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)