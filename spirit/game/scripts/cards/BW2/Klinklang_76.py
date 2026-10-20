from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard


async def zap_cannon(ctx):
    """80 damage. Flip; if tails, can't use Zap Cannon next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and not results[0] and ctx.ability.ability_id:
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id, ctx.ability.ability_id,
        )


card = PokemonCardDef(
    guid="e66feb3c-65c1-575e-b3d1-a077f412e5f6",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=attach_from_discard(),
        ),
        Attack(
            title="Zap Cannon",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=zap_cannon,
        ),
    ],
)
