from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.session.effects import full_stack


def _star_guardian_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    prizes = board.find_player_area(opponent_id, "prizePile")
    bench = board.find_player_area(opponent_id, "bench")
    return bool(prizes) and len(prizes.children) == 1 and bool(bench and bench.children)


async def star_guardian(ctx):
    """VSTAR Power: if the opponent has exactly 1 Prize left, you may make
    them discard 1 of their Benched Pokemon and all attached cards."""
    if not await ctx.ask_yes_no(
        "Choose 1 of your opponent's Benched Pokémon? They discard that "
        "Pokémon and all attached cards."
    ):
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    await ctx.discard_cards(full_stack(target))


async def giga_impact(ctx):
    """230. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="0e4aa482-8295-5b75-b012-daf58cb96397",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasVSTAR.Name",
    display_name="Regigigas VSTAR",
    searchable_by=["Regigigas VSTAR", "VSTAR", "RegigigasVSTAR"],
    subtypes=["VSTAR"],
    collector_number=114,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasV.Name",
    family_id=486,
    abilities=[
        Ability(
            title="Star Guardian",
            game_text="During your turn, if your opponent has exactly 1 Prize card remaining, you may choose 1 of your opponent's Benched Pok\u00e9mon. They discard that Pok\u00e9mon and all attached cards. (You can't use more than 1 VSTAR Power in a game.)",
            vstar=True,
            condition=_star_guardian_condition,
            effect=star_guardian,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=giga_impact,
        ),
    ],
)