from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_protection
from spirit.game.card_effects.attacks_common import snipe_attack


async def _mist_concealment(ctx):
    """When you evolve into this Pokemon from your hand: you may prevent all
    effects of attacks, including damage, done to it during the opponent's next turn."""
    if await ctx.ask_yes_no("Use Mist Concealment?"):
        await apply_protection(ctx, target=ctx.source, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="689f4414-0cae-56c2-9c44-918350bde9bc",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja",
    searchable_by=["Greninja", "Stage 2", "Greninja"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    abilities=[
        Ability(
            title="Mist Concealment",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon during your opponent's next turn.",
            trigger=Triggers.ON_EVOLVE,
            effect=_mist_concealment,
        ),
        Attack(
            title="Shadow Bullet",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=snipe_attack(20, also_base=True),
        ),
    ],
)