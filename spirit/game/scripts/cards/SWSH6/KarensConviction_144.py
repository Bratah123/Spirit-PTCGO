from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def karens_conviction(ctx):
    """This turn, your Single Strike Pokemon's attacks do 20 more damage to
    the opponent's Active Pokemon for each Prize the opponent has taken."""
    taken = ctx.prizes_taken(ctx.opponent_id)
    if taken <= 0:
        return
    amount = 20 * taken
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(amount, ctx.player_id, requires_subtype="Single Strike")
    )
    for pokemon in ctx.my_pokemon_in_play():
        if "Single Strike" in subtypes_for(pokemon.archetype_id):
            await ctx.add_stat_visualization(
                pokemon, "Positive", "DamageDealtIncreased",
                card_text=f"+{amount} damage")


card = SupporterCardDef(
    guid="2bd1b1d0-660b-53b4-8168-308b34b8a82e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KarensConviction.Name",
    display_name="Karen's Conviction",
    searchable_by=["Karen's Conviction", "Supporter", "Single Strike"],
    subtypes=["Supporter", "Single Strike"],
    collector_number=144,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=karens_conviction
)
