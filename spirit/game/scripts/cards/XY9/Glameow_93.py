from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _act_cute(ctx):
    """Your opponent puts a card from their hand on the bottom of their deck."""
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    pick = await ctx.choose_cards(hand, 1, minimum=1, prompt="Put a card on the bottom of your deck",
                                  player_id=ctx.opponent_id)
    if pick:
        await ctx.put_on_bottom_of_deck(pick[0])


card = PokemonCardDef(
    guid="6ab9a3c9-bf2a-579f-b1e1-5debe87754e7",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    display_name="Glameow",
    searchable_by=["Glameow", "Basic", "Glameow"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=431,
    abilities=[
        Attack(
            title="Act Cute",
            game_text="Your opponent puts a card from his or her hand on the bottom of his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_act_cute,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)