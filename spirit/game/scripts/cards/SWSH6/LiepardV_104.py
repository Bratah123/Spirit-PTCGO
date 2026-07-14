from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play


async def hidden_claw(ctx):
    """On play from hand to bench: you may discard a Pokémon Tool from a Pokémon (either side)."""
    tools = [(t, p) for t, p in ctx.tools_in_play()
             if p.owning_player_id == ctx.player_id or not ctx.effects_blocked(p)]
    if not tools:
        return
    if not await ctx.ask_yes_no("Discard a Pokémon Tool from a Pokémon?"):
        return
    tool_cards = [t for t, p in tools]
    picks = await ctx.choose_cards(tool_cards, 1, prompt="Choose a Pokémon Tool to discard")
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="b1d03ddd-7a00-5126-af3a-e23cec56bb8b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LiepardV.Name",
    display_name="Liepard V",
    searchable_by=["Liepard V", "Basic", "V", "LiepardV"],
    subtypes=["Basic", "V"],
    collector_number=104,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=510,
    abilities=[
        Ability(
            title="Hidden Claw",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Pok\u00e9mon Tool from a Pok\u00e9mon (yours or your opponent's).",
            trigger=Triggers.ON_PLAY,
            effect=hidden_claw,
        ),
        Attack(
            title="Shadow Ripper",
            game_text="You may put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=remove_self_from_play(destination="hand", with_attachments="same", optional=True),
        ),
    ],
)