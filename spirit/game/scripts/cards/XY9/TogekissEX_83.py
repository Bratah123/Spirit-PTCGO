from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card


async def _mighty_wind(ctx):
    """20; you may attach an Energy card from your hand to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not bench or not pool:
        return
    pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach an Energy card? (optional)")
    if not pick:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Attach to which Benched Pokémon?")
    await ctx.attach_energy(pick[0], target or bench[0])


card = PokemonCardDef(
    guid="3c31c80a-7218-5b14-afe9-df18ec63c089",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissEX.Name",
    display_name="Togekiss-EX",
    searchable_by=["Togekiss-EX", "Basic", "EX", "TogekissEX"],
    subtypes=["Basic", "EX"],
    collector_number=83,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=468,
    abilities=[
        Attack(
            title="Mighty Wind",
            game_text="You may attach an Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=_mighty_wind,
        ),
        Attack(
            title="Hurricane Wing",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)