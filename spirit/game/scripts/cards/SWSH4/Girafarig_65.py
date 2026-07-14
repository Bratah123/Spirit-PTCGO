from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


async def commanding_tail(ctx):
    """30. You may have your opponent shuffle their hand into their deck. If you do, your opponent draws 4 cards."""
    await ctx.deal_damage()
    if await ctx.ask_yes_no(
        "Have your opponent shuffle their hand into their deck? If you do, your opponent draws 4 cards."
    ):
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
        await ctx.draw_cards(4, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="7940396c-6459-5205-aa08-2e7740c3d027",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=203,
    abilities=[
        Attack(
            title="Psypower",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(2, "choose_any_opponent"),
        ),
        Attack(
            title="Commanding Tail",
            game_text="You may have your opponent shuffle their hand into their deck. If you do, your opponent draws 4 cards.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=commanding_tail,
        ),
    ],
)