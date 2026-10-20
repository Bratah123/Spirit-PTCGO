"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Seviper (TATM #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba7b8ffa-8af8-54f9-a135-3ec608b2590e",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSeviper.Name",
    display_name="Team Aqua's Seviper",
    searchable_by=["Team Aqua's Seviper", "Basic", "TeamAquasSeviper"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Venomous Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Venom Tail",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, discard an Energy attached to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)