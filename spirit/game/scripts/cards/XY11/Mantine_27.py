from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _healing_wave(ctx):
    """Discard any number of cards from your hand; heal 10 per card from this Pokemon."""
    hand = ctx.hand()
    picked = await ctx.choose_cards(hand, len(hand), minimum=0, prompt="Discard any cards from your hand") if hand else []
    if picked:
        await ctx.discard_cards(picked)
        await ctx.heal(10 * len(picked), ctx.attacker)


async def _dwindling_wave(ctx):
    """90 minus 10 for each damage counter on this Pokemon."""
    await ctx.deal_damage(max(0, 90 - 10 * damage_counters_on('self')(ctx)))


card = PokemonCardDef(
    guid="5f42b244-b2e3-5479-8b77-6a02091f15e7",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=226,
    abilities=[
        Attack(
            title="Healing Wave",
            game_text="Discard as many cards as you like from your hand. Heal 10 damage from this Pok\u00e9mon for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            effect=_healing_wave,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="This attack does 90 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=90,
            damage_operator="-",
            effect=_dwindling_wave,
        ),
    ],
)