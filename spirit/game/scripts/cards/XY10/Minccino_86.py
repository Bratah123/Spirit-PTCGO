from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _tools(p):
    return [c for c in p.children if c.get_attribute(AttrID.TRAINER_TYPE) in
            (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)]


async def _cleaning_up(ctx):
    """Discard a Pokemon Tool card attached to 1 of your opponent's Pokemon."""
    pool = [p for p in ctx.opponent_pokemon_in_play() if _tools(p) and not ctx.effects_blocked(p)]
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Discard a Tool from which Pokémon?")
    tools = _tools(target) if target is not None else []
    if tools:
        pick = tools if len(tools) == 1 else await ctx.choose_cards(tools, 1, minimum=1, prompt="Choose a Tool")
        if pick:
            await ctx.discard_cards(pick[:1])


card = PokemonCardDef(
    guid="ba9bd381-05db-5a6a-b366-4c494d7887cd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Cleaning Up",
            game_text="Discard a Pok\u00e9mon Tool card attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_cleaning_up,
        ),
    ],
)