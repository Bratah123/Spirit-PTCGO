from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


async def _rescue(ctx):
    """Shuffle 3 Pokemon from your discard pile into your deck."""
    cards = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 3, prompt="Choose 3 Pokémon to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = PokemonCardDef(
    guid="982095b1-a0ad-5320-b161-997441223598",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1", "Floatzel"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Rescue",
            game_text="Shuffle 3 Pok\u00e9mon from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_rescue,
        ),
        Attack(
            title="Screw Tail",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=_flip_discard_defender_energy,
        ),
    ],
)