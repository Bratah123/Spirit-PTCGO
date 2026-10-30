"""STUB: effect not implemented — do not guess mechanics.
Darkrai (DPP #DP24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import spacial_rend


card = PokemonCardDef(
    guid="16f6f3bd-3789-5db2-a9b3-6f3b42ee9a63",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Attack(
            title="Spacial Rend",
            game_text="Search your deck for a Stadium card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. If there is any Stadium card in play, discard it.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=spacial_rend(),
        ),
        Attack(
            title="Roar of Time",
            game_text="Search your discard pile for 3 Pok\u00e9mon, show them to your opponent, and put them on top of your deck. Shuffle your deck afterward. (If you don't have 3 Pok\u00e9mon in your discard pile, this attack does nothing.)",
            cost={PokemonTypes.METAL: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)