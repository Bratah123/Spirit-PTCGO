from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def borne_ashore(ctx):
    """Put a Basic Pokémon from either discard pile onto its owner's Bench."""
    pool = [
        c for pid in (ctx.player_id, ctx.opponent_id)
        for c in ctx.discard_pile(pid) if is_basic_pokemon(c)
    ]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto its owner's Bench",
    )
    if not picks:
        return
    card = picks[0]
    owner = card.owning_player_id or ctx.player_id
    if len(ctx.board.find_player_area(owner, "bench").children) >= effective_bench_capacity(ctx.board, owner):
        return
    await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="40dde91f-4344-541d-9fa5-77f488ef5897",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=594,
    abilities=[
        Attack(
            title="Borne Ashore",
            game_text="Put a Basic Pok\u00e9mon from either player's discard pile onto its owner's Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=borne_ashore,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)