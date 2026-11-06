from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand, flip_bonus


async def knock_off(ctx):
    """discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="ab7e4d53-e91d-5466-bb31-d76936b65429",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Team Plasma", "Watchog"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=112,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Fast Swipe",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=knock_off,
        ),
        Attack(
            title="Biting Fang",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)