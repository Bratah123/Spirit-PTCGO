from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _mental_trash(ctx):
    """Your opponent flips 4 coins; for each tails they discard a card from
    their hand (they choose)."""
    results = await ctx.flip_coins(4, ctx.ability.title) or []
    tails = sum(1 for r in results if not r)
    hand = ctx.hand(ctx.opponent_id)
    n = min(tails, len(hand))
    if n:
        await ctx.discard_from_hand(n, minimum=n, player_id=ctx.opponent_id,
                                    prompt="Choose cards to discard")


card = PokemonCardDef(
    guid="d4441e4d-bde6-50d9-bf3f-eefd11340063",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Mental Trash",
            game_text="Your opponent flips 4 coins. For each tails, he or she discards a card from his or her hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_mental_trash,
        ),
        Attack(
            title="Distortion Beam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep. If tails, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True, tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)