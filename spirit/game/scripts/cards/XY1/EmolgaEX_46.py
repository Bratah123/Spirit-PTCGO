"""STUB: effect not implemented — do not guess mechanics.
Emolga-EX (XY1 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="256fe356-5a0a-5782-b2ae-f06a273ab98c",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmolgaEX.Name",
    display_name="Emolga-EX",
    searchable_by=["Emolga-EX", "Basic", "EX", "EmolgaEX"],
    subtypes=["Basic", "EX"],
    collector_number=46,
    set_code="XY1",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=587,
    abilities=[
        Attack(
            title="Energy Glide",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward. If you attached Energy in this way, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electron Crush",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)