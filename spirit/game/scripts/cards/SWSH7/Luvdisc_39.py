from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def synchrodraw(ctx):
    """Shuffle your hand into your deck. Then, draw a card for each card in
    your opponent's hand."""
    draw_count = ctx.hand_size(ctx.opponent_id)
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(draw_count)


card = PokemonCardDef(
    guid="c247656d-7fa8-57db-9178-7dff92d38c86",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Synchrodraw",
            game_text="Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=synchrodraw,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)