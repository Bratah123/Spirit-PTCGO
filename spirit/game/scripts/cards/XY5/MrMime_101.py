from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import tool_slots_free


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def _trick(ctx):
    """Move a Tool on 1 of either player's Pokemon to another of that player's
    Pokemon without a Tool; does nothing if there is nowhere to move it."""
    options = []
    for pid in (ctx.player_id, ctx.opponent_id):
        mons = ctx.board.pokemon_in_play(pid)
        for p in mons:
            for t in p.children:
                if _is_tool(t) and any(q is not p and tool_slots_free(ctx.board, q) > 0 for q in mons):
                    options.append(t)
    if not options:
        return
    picks = await ctx.choose_cards(options, 1, minimum=1, prompt="Choose a Pokémon Tool to move")
    if not picks:
        return
    tool = picks[0]
    holder = tool.parent
    dests = [q for q in ctx.board.pokemon_in_play(holder.owning_player_id)
             if q is not holder and tool_slots_free(ctx.board, q) > 0]
    if not dests:
        return
    dest = dests[0] if len(dests) == 1 else await ctx.choose_pokemon(dests, "Move it to which Pokémon?")
    await ctx.attach_tool(tool, dest or dests[0])


card = PokemonCardDef(
    guid="74c179dd-4c5e-5664-89e4-af50938fc9dd",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title="Trick",
            game_text="Move a Pok\u00e9mon Tool card attached to 1 of either player's Pok\u00e9mon to another of that player's Pok\u00e9mon that doesn't already have a Pok\u00e9mon Tool attached to it. If there is no Pok\u00e9mon to move the Pok\u00e9mon Tool card to, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_trick,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)