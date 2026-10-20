from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy


async def _final_wish(ctx):
    """When this Pokemon is Knocked Out by damage from an opponent's attack,
    search your deck for a card and put it into your hand; shuffle."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _seafaring(ctx):
    """Flip 3 coins. For each heads, attach a Water Energy card from your
    discard pile to your Benched Pokemon in any way you like."""
    heads = sum(1 for r in await ctx.flip_coins(3, ctx.ability.title) if r)
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if _is_water_energy(c)]
    n = min(heads, len(pool))
    if n <= 0 or not bench:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Water Energy cards to attach")
    await distribute_energy(ctx, picks, bench)


card = PokemonCardDef(
    guid="7d90b453-bc4c-53a4-8d97-d84ddccc3a46",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Final Wish",
            game_text="When this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_final_wish,
        ),
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=_seafaring,
        ),
    ],
)