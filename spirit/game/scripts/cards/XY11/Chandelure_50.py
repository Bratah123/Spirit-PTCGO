from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard
from spirit.game.session.effects import is_supporter_card


def _sinister_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def _sinister_selection(ctx):
    """Look at the top 2 cards of your deck; put 1 into your hand and discard the other."""
    top = ctx.deck_top(2)
    if not top:
        return
    keep = await ctx.choose_cards(top, 1, minimum=1, prompt="Choose a card to put into your hand")
    if keep:
        await ctx.put_in_hand(keep, reveal=False)
    rest = [c for c in top if c not in keep]
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="474330c2-b16b-54da-b78d-c6ef27173fd1",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Sinister Selection",
            game_text="Once during your turn (before your attack), you may look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sinister_condition,
            effect=_sinister_selection,
        ),
        Attack(
            title="Past Friends",
            game_text="This attack does 10 more damage for each Supporter card in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_discard("mine", is_supporter_card), 10, base=10),
        ),
    ],
)