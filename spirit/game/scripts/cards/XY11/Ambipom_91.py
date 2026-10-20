from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card


async def _furry_chance(ctx):
    """Discard the top card of the opponent's deck; +60 if it is an Energy card."""
    top = ctx.deck_top(1, ctx.opponent_id)
    bonus = 0
    if top:
        await ctx.discard_cards(top)
        bonus = 60 if is_energy_card(top[0]) else 0
    await ctx.deal_damage(20 + bonus)


card = PokemonCardDef(
    guid="bd6d3e01-5ebe-54ea-b41a-9bbb4a398b5a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="Furry Chance",
            game_text="Discard the top card of your opponent's deck. If that card is an Energy card, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=_furry_chance,
        ),
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(2, per_heads=50),
        ),
    ],
)