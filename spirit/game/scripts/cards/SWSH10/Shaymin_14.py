from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand


def _only_turn_2(board, player_id, pokemon):
    return board.turn_state.turn_number == 2


card = PokemonCardDef(
    guid="5db6b80a-4feb-5c5a-8b22-2164a12a96a7",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Encouraging Gift",
            game_text="You can use this attack only if you go second, and only during your first turn. Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_only_turn_2,
            effect=search_to_hand(count=3, minimum=0, reveal=False,
                                  prompt="Choose up to 3 cards."),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)