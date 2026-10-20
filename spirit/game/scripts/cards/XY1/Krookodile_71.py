from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.session.effects import is_supporter_card


async def _bother(ctx):
    """50; flip a coin. If heads, your opponent can't play Supporter cards
    from their hand during their next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        ctx.lock_plays(ctx.opponent_id, is_supporter_card)


card = PokemonCardDef(
    guid="ee50649b-e6cf-5571-9a58-db294e4631d8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Krookodile"],
    subtypes=["Stage 2"],
    collector_number=71,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Bother",
            game_text="Flip a coin. If heads, your opponent can't play any Supporter cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_bother,
        ),
        Attack(
            title="Knock Back",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)