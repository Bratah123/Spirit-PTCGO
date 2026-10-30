"""STUB: effect not implemented — do not guess mechanics.
Feebas (DP4 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import evolution_impulse_search


card = PokemonCardDef(
    guid="9e71bfba-ffb3-5840-8137-d28c9b57a14a",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="DP4",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Fast Evolution",
            game_text="Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=evolution_impulse_search(),
        ),
    ],
)