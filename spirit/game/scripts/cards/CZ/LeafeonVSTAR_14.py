from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive


def _ivy_star_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    bench = board.find_player_area(opponent_id, "bench")
    return bool(board.active_pokemon(opponent_id)) and bool(bench and bench.children)


async def ivy_star(ctx):
    """You may switch 1 of your opponent's Benched Pokémon with their Active
    Pokémon."""
    opp_active = ctx.opponent_active()
    opp_bench = ctx.opponent_bench()
    if opp_active is None or not opp_bench or ctx.effects_blocked(opp_active):
        return
    if not await ctx.ask_yes_no(
        "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"
    ):
        return
    target = await ctx.choose_pokemon(
        opp_bench, "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def leaf_guard(ctx):
    """180. During your opponent's next turn, this Pokémon takes 30 less
    damage from attacks (after applying Weakness and Resistance)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(30))


card = PokemonCardDef(
    guid="1c418037-55c4-561c-b98b-acb0a20099c0",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVSTAR.Name",
    display_name="Leafeon VSTAR",
    searchable_by=["Leafeon VSTAR", "VSTAR", "LeafeonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=14,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Ability(
            title="Ivy Star",
            game_text="During your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            vstar=True,
            condition=_ivy_star_condition,
            effect=ivy_star,
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=leaf_guard,
        ),
    ],
)