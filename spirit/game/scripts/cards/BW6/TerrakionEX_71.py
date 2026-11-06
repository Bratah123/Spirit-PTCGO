from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _pump_up_smash(ctx):
    """Printed damage, then attach up to 2 basic Energy cards from your hand
    to your Benched Pokemon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Choose up to 2 basic Energy cards to attach")
    if picks:
        await distribute_energy(ctx, picks, bench)


card = PokemonCardDef(
    guid="4a60b9bd-115a-506b-82c2-11cfedc54886",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TerrakionEX.Name",
    display_name="Terrakion-EX",
    searchable_by=["Terrakion-EX", "Basic", "EX", "TerrakionEX"],
    subtypes=["Basic", "EX"],
    collector_number=71,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=feint,
        ),
        Attack(
            title="Pump-up Smash",
            game_text="Attach 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_pump_up_smash,
        ),
    ],
)