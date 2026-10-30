"""STUB: effect not implemented — do not guess mechanics.
Slowking (EX10 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import item_search_tool, aftermath_tools

card = PokemonCardDef(
    guid="71ecfa15-40cb-5ef8-95bb-2baa81d36dfc",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Item Search",
            game_text="Once during your turn (before your attack), you may search your deck for a Pok\u00e9mon Tool card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Slowking is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            # STUB: ability effect not implemented
            effect=item_search_tool(),
        ),
        Attack(
            title="Aftermath",
            game_text="Does 20 damage plus 10 more damage for each Pok\u00e9mon Tool card in your discard pile. You can't add more than 60 damage in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=aftermath_tools(20, 10, 60),
        ),
    ],
)