from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


card = PokemonCardDef(
    guid="2eeeb7a7-f2be-5a79-bfc3-271ac56b4287",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=668,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_flip_discard_defender_energy,
        ),
        Attack(
            title="Royal Flare",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)