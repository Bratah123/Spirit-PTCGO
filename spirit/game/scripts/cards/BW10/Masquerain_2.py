from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID, TrainerType


def _tools_on(pokemon):
    return [c for c in pokemon.children
            if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]


def _tool_reversal_condition(board, player_id, pokemon=None):
    return any(_tools_on(p) for p in board.pokemon_in_play(player_id))


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
    guid="b309100b-2846-5fa2-ad95-e60d102f1cb2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Team Plasma", "Masquerain"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=2,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Ability(
            title="Tool Reversal",
            game_text="As often as you like during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to 1 of your Pok\u00e9mon into your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_tool_reversal_condition,
            effect=_tool_reversal,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)