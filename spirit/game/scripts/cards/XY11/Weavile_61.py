from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _tool_reversal_condition(board, player_id, pokemon=None):
    return any(_tools_on(p) for p in board.pokemon_in_play(player_id))


def _tools_on(pokemon):
    return [c for c in pokemon.children
            if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]


async def _tool_reversal(ctx):
    """As often as you like during your turn, put a Pokemon Tool card attached
    to 1 of your Pokemon into your hand."""
    tools = [t for p in ctx.my_pokemon_in_play() for t in _tools_on(p)]
    if not tools:
        return
    picks = await ctx.choose_cards(tools, 1, minimum=1, prompt="Choose a Pokémon Tool to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="9371c31d-973a-510b-ac31-fef489b9fe09",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Tear Away",
            game_text="As often as you like during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to 1 of your Pok\u00e9mon into your hand.",
            activation=Activations.UNLIMITED,
            condition=_tool_reversal_condition,
            effect=_tool_reversal,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)