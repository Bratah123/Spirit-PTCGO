from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def _tentacle_condition(board, player_id, pokemon=None):
    opp = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opp, "bench") if opp else None
    return bool(bench) and any(_is_ex(p) for p in bench.children)


async def _dangerous_tentacle(ctx):
    """Switch 1 of your opponent's Benched Pokemon-EX with their Active Pokemon."""
    pool = [p for p in ctx.opponent_bench() if _is_ex(p)]
    if pool:
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Benched Pokémon-EX")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="a1f6e027-6fc0-53d3-baa7-28bc29f5ca4f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OmastarBREAK.Name",
    display_name="Omastar BREAK",
    searchable_by=["Omastar BREAK", "BREAK", "OmastarBREAK"],
    subtypes=["BREAK"],
    collector_number=19,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Dangerous Tentacle",
            game_text="Once during your turn (before your attack), you may switch 1 of your opponent's Benched Pok\u00e9mon-EX with his or her Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_tentacle_condition,
            effect=_dangerous_tentacle,
        ),
    ],
)