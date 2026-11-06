from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand, flip_damage


async def knock_off(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="e00b9e86-7bf2-59a2-a578-85a12e58ea75",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1", "Escavalier"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Poke Through",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=knock_off,
        ),
        Attack(
            title="Spiral Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)