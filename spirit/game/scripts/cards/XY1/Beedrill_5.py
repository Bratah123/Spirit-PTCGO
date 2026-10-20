from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import apply_protection


async def _flash_needle(ctx):
    """Flip 3 coins: 40 per heads; all heads -> prevent all effects of attacks,
    including damage, done to this Pokemon during the opponent's next turn."""
    results = await ctx.flip_coins(3, ctx.ability.title) or []
    heads = sum(1 for r in results if r)
    await ctx.deal_damage(40 * heads)
    if results and heads == len(results) == 3:
        await apply_protection(ctx, target=ctx.attacker, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="5963bb27-70a0-5fc0-91b3-b486f80897e9",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Flash Needle",
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads. If all of them are heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator="x",
            effect=_flash_needle,
        ),
    ],
)