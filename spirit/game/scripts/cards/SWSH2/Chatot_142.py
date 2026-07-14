from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card


async def lucky_match(ctx):
    if not await ctx.ask_yes_no("Flip a coin for Lucky Match?"):
        return
    heads = (await ctx.flip_coins(1, "Lucky Match"))[0]
    if not heads:
        return
    supporters = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not supporters:
        return
    picks = await ctx.choose_cards(
        supporters, 1, minimum=1,
        prompt="Choose a Supporter card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="a175066a-4e1b-5f72-9144-dea4a170053d",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Ability(
            title="Lucky Match",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may flip a coin. If heads, put a Supporter card from your discard pile into your hand.",
            trigger=Triggers.ON_PLAY,
            effect=lucky_match,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
