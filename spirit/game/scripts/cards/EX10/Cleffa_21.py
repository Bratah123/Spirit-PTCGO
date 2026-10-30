"""STUB: effect not implemented — do not guess mechanics.
Cleffa (EX10 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition


card = PokemonCardDef(
    guid="61da1619-d6c3-5065-8f23-816cb0cbf3a7",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=173,
    abilities=[
        Ability(
            title="Baby Evolution",
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition("Clefairy"),
            game_text="Once during your turn (before your attack), you may put Clefairy from your hand onto Cleffa (this counts as evolving Cleffa) and remove all damage counters from Cleffa.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=baby_evolution("Clefairy"),
        ),
        Attack(
            title="Eeeeeeek",
            game_text="Shuffle your hand into your deck, then draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=shuffle_hand_into_deck_draw(6),
        ),
    ],
)