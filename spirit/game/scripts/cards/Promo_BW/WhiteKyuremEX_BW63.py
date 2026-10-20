from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def _dragon_stream(ctx):
    """Printed damage. Flip a coin; if heads attach a basic Energy card from
    your discard pile to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Dragon Stream")
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not results or not results[0] or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a basic Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


async def _burn_defender(ctx):
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="351931d6-2241-54b2-883d-fc9805e20570",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremEX.Name",
    display_name="White Kyurem-EX",
    searchable_by=["White Kyurem-EX", "Basic", "EX", "WhiteKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=63,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Dragon Stream",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_dragon_stream,
        ),
        Attack(
            title="Ice Burn",
            game_text="Discard 2 Fire Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE, also=_burn_defender),
        ),
    ],
)