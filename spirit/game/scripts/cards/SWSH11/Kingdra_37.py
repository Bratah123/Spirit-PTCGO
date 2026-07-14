from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _seething_currents(ctx):
    """You may have either player shuffle their hand into their deck; if
    they did, they draw 4 cards."""
    if not await ctx.ask_yes_no(
        "Have either player shuffle their hand and put it on the bottom of their deck?"
    ):
        return
    choice = await ctx.choose(
        "Choose a player to shuffle their hand into their deck.",
        ["You", "Your Opponent"], use_panel=False,
    )
    target_id = ctx.player_id if choice == 0 else ctx.opponent_id
    moved = await ctx.hand_to_bottom_of_deck(target_id)
    if moved:
        await ctx.draw_cards(4, player_id=target_id)

card = PokemonCardDef(
    guid="8552ac38-d4fa-581b-8e31-2d582efdf008",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Seething Currents",
            game_text="Once during your turn, you may have either player shuffle their hand and put it on the bottom of their deck. If that player put any cards on the bottom of their deck in this way, they draw 4 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=_seething_currents,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)