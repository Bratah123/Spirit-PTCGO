from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.effects import is_pokemon_card


async def _whisk_away(ctx):
    """30+; the opponent reveals their hand; put a Pokemon from it on the
    bottom of their deck. If you do, +30."""
    cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    pool = [c for c in cards or [] if is_pokemon_card(c)]
    bonus = 0
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Pokémon to put on the bottom of your opponent's deck")
        if picks and await ctx.put_on_bottom_of_deck(picks[0]):
            bonus = 30
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="cc42f256-9d42-50e7-8186-1d6d90d7e61a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=275,
    abilities=[
        Attack(
            title="Whisk Away",
            game_text="Your opponent reveals his or her hand. Choose a Pok\u00e9mon you find there and put it on the bottom your opponent's deck. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=_whisk_away,
        ),
        Attack(
            title="Spirit Dance",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)