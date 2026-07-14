from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def package_delivery(ctx):
    """Put this Pokemon and all attached cards into the deck. If you do,
    search your deck for a card and put it into your hand. Shuffle."""
    await ctx.shuffle_into_deck(full_stack(ctx.source), ctx.player_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)
    picks = await ctx.search_deck(
        None, count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="6557db9b-47b6-5c5d-93d6-bfe7e1e65662",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Package Delivery",
            game_text="Put this Pok\u00e9mon and all attached cards into your deck. If you do, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=package_delivery,
        ),
    ],
)