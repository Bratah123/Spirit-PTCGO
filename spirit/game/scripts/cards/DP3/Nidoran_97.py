"""STUB: effect not implemented — do not guess mechanics.
Nidoran ♂ (DP3 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b55da96a-990b-5f49-82cb-627acc0b6db1",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran \u2642", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Skin",
            game_text="Flip 2 coins. If either of them is heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)