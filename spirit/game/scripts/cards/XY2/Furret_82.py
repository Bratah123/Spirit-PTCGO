from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _buried_treasure_hunt(ctx):
    """Look at the top 4 cards of your deck, put 2 into your hand, discard the rest."""
    top = ctx.deck_top(4)
    if not top:
        return
    picks = await ctx.choose_cards(top, 2, prompt="Choose 2 cards to put into your hand") or []
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="f490ee89-e017-5d4a-9473-74ba88628a87",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Buried Treasure Hunt",
            game_text="Look at the top 4 cards of your deck and put 2 of them into your hand. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_buried_treasure_hunt,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)