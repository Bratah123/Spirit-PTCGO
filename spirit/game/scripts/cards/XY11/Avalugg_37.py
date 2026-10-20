from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _melting_floe(ctx):
    """Discard the top 3 cards of your deck; for each Water Energy card, discard
    the top 3 cards of your opponent's deck."""
    top = ctx.deck_top(3)
    if not top:
        return
    await ctx.discard_cards(top)
    n = sum(1 for c in top if _is_water_energy(c))
    if n:
        mill = ctx.deck_top(3 * n, ctx.opponent_id)
        if mill:
            await ctx.discard_cards(mill)


card = PokemonCardDef(
    guid="3c7117bd-63c8-551d-852d-f0af0732b491",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name",
    display_name="Avalugg",
    searchable_by=["Avalugg", "Stage 1", "Avalugg"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_flip_discard_defender_energy,
        ),
        Attack(
            title="Melting Floe",
            game_text="Discard the top 3 cards of your deck. For each Water Energy card you discarded in this way, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.WATER: 3},
            effect=_melting_floe,
        ),
    ],
)