from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _startling_bark(ctx):
    """Flip: heads, 3 random cards from your opponent's hand are revealed and shuffled into their deck."""
    import random
    results = await ctx.flip_coins(1, ctx.ability.title)
    hand = list(ctx.hand(ctx.opponent_id))
    if results and results[0] and hand:
        picks = random.sample(hand, min(3, len(hand)))
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="710bf233-4a6a-5c1f-a4a8-47b22e628824",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Attack(
            title="Startling Bark",
            game_text="Flip a coin. If heads, choose 3 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_startling_bark,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)