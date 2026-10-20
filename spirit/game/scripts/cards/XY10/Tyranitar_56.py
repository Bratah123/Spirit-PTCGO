from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_supporter_card


def _is_dark_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


_taken = count_prizes_taken('opponent')


async def _raging_roar(ctx):
    """On evolve from hand: attach 1 Darkness Energy from your discard per Prize your opponent has taken."""
    n = _taken(ctx)
    pool = [c for c in ctx.discard_pile() if is_energy_card(c) and _is_dark_energy(c)]
    n = min(n, len(pool))
    if not n or not await ctx.ask_yes_no("Use Raging Roar?"):
        return
    picks = await ctx.choose_cards(pool, n, minimum=0, prompt="Choose Darkness Energy to attach")
    for e in picks or []:
        await ctx.attach_energy(e, ctx.source)


async def _dark_mountain(ctx):
    """150+; discard your top 2 cards; 50 more per Supporter discarded."""
    top = ctx.deck_top(2)
    if top:
        await ctx.discard_cards(top)
    await ctx.deal_damage(ctx.ability.damage + 50 * sum(1 for c in top if is_supporter_card(c)))


card = PokemonCardDef(
    guid="abc94f0b-1003-5b62-9167-a8be94fcf646",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Raging Roar",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may attach 1 Darkness Energy from your discard pile to this Pok\u00e9mon for each Prize card your opponent has taken.",
            trigger=Triggers.ON_EVOLVE,
            effect=_raging_roar,
        ),
        Attack(
            title="Dark Mountain",
            game_text="Discard the top 2 cards of your deck. This attack does 50 more damage for each Supporter card discarded in this way.",
            cost={PokemonTypes.DARKNESS: 5},
            damage=150,
            damage_operator="+",
            effect=_dark_mountain,
        ),
    ],
)