from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import look_at_top


def _forewarn_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="51056405-816e-5a08-9f89-6d97b5311960",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Ability(
            title="Forewarn",
            game_text="Once during your turn (before your attack), you may look at the top 2 cards of your deck, choose 1 of them, and put it into your hand. Put the other card back on top of your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_forewarn_condition,
            effect=look_at_top(2, take=1, rest='back',
                              prompt='Choose a card to put into your hand.'),
        ),
        Attack(
            title="Fluffy Dream",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)