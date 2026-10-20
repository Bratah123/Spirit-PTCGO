from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="7ddac4f9-3b5d-5069-b017-f3e9e9b5d48b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MPidgeotEX.Name",
    display_name="M Pidgeot-EX",
    searchable_by=["M Pidgeot-EX", "MEGA", "EX", "MPidgeotEX"],
    subtypes=["MEGA", "EX"],
    collector_number=65,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotEX.Name",
    family_id=18,
    abilities=[
        Attack(
            title="Mach Cyclone",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=push_down,
        ),
    ],
)