from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def ominous_prose(ctx):
    """Opponent reveals their hand. If 4+ cards, choose all but 3 to shuffle
    into their deck."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    if len(hand) < 4:
        return
    count = len(hand) - 3
    picks = await ctx.choose_cards(
        hand, count, minimum=count,
        prompt="Choose cards to shuffle into your opponent's deck.",
        player_id=ctx.player_id,
    )
    await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="5ed2291a-5cbc-5c99-98fb-b3478a403378",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Attack(
            title="Ominous Prose",
            game_text="Your opponent reveals their hand. If they have 4 or more cards in their hand, choose all but 3, and your opponent shuffles the chosen cards into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ominous_prose,
        ),
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)