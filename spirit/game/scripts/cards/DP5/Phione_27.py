"""STUB: effect not implemented — do not guess mechanics.
Phione (DP5 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import charm_reduce_defender_next
from spirit.game.card_effects.dp import dp3_vibrava_74_hyper_beam


card = PokemonCardDef(
    guid="4c28322d-3231-5f20-b9e4-e1d54b4117ba",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Charm",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=charm_reduce_defender_next(20),
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=dp3_vibrava_74_hyper_beam(),
        ),
    ],
)