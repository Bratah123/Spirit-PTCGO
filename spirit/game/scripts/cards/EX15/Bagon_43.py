"""STUB: effect not implemented — do not guess mechanics.
Bagon δ (EX15 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import granite_head
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92d9e9c5-d485-5190-98dd-fa368e1e1b29",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon δ",
    searchable_by=["Bagon \u03b4", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=371,
    abilities=[
        Attack(
            title="Granite Head",
            game_text="During your opponent's next turn, any damage done to Bagon by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=granite_head(),
        ),
    ],
)