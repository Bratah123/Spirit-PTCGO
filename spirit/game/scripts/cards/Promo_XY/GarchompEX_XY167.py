from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import shred


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
    guid="2e3d52c9-0375-52ad-b5d9-afa2504f0714",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name",
    display_name="Garchomp-EX",
    searchable_by=["Garchomp-EX", "Basic", "EX", "GarchompEX"],
    subtypes=["Basic", "EX"],
    collector_number=167,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=shred,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_flip_discard_defender_energy,
        ),
    ],
)