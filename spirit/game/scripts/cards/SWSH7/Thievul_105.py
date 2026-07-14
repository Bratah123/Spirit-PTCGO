from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _fumbling_hands(ctx):
    if not await ctx.ask_yes_no(
        "Have each player shuffle their hand into their deck?"
    ):
        return
    moved_mine = await ctx.hand_to_bottom_of_deck(ctx.player_id)
    moved_opp = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if not (moved_mine or moved_opp):
        return
    await ctx.draw_cards(4, ctx.player_id)
    await ctx.draw_cards(4, ctx.opponent_id)


card = PokemonCardDef(
    guid="2d50e350-f893-59c0-8737-1a348f784c32",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1", "Thievul"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Ability(
            title="Fumbling Hands",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have each player shuffle their hand and put it on the bottom of their deck. If either player put any cards on the bottom of their deck in this way, each player draws 4 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=_fumbling_hands,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)