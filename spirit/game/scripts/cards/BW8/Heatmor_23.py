from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import gust_then
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _burn_new_active(ctx, new_active):
    """The new Defending Pokemon is now Burned."""
    if new_active is not None and not ctx.effects_blocked(new_active):
        await ctx.apply_special_condition(new_active, SpecialConditions.BURNED)


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _fiery_licks(ctx):
    """Discard the top 4 cards of your deck; 50 damage times the number of
    Fire Energy cards discarded."""
    top = ctx.deck_top(4)
    if top:
        await ctx.discard_cards(top)
    await ctx.deal_damage(50 * sum(1 for c in top if _is_fire_energy(c)))


card = PokemonCardDef(
    guid="140e4025-a3a1-5cf7-b0e2-441cccdd9cb0",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Luring Flame",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=gust_then(_burn_new_active),
        ),
        Attack(
            title="Fiery Licks",
            game_text="Discard the top 4 cards of your deck. This attack does 50 damage times the number of Fire Energy cards discarded.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=_fiery_licks,
        ),
    ],
)