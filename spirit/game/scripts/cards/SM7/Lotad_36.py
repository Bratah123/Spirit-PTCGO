from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
import random


async def astonish(ctx):
    """Choose a random card from the opponent's hand, reveal it, shuffle into their deck."""
    await ctx.deal_damage()
    opponent = ctx.opponent_id
    hand = ctx.hand(opponent)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], player_id=opponent)


card = PokemonCardDef(
    guid="0e3ef561-c958-5c4c-b759-b5d7ce449b7f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    display_name="Lotad",
    searchable_by=["Lotad", "Basic", "Lotad"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=270,
    abilities=[
        Attack(
            title="Surprise",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=astonish,
        ),
    ],
)