from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import in_active_spot, is_energy_card


async def _woodland_stroll(ctx):
    if not await ctx.ask_yes_no("Look at the top 6 cards of your deck?"):
        return
    top = ctx.deck_top(6)
    if not top:
        return
    candidates = [c for c in top if is_energy_card(c)]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0,
            prompt="Reveal an Energy card you find there and put it into your hand.",
            display_cards=top,
        )
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8ec72ba1-63a1-553d-b33a-af5c8a261e6a",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SWSH45",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Woodland Stroll",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 6 cards of your deck, reveal an Energy card you find there, and put it into your hand. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=_woodland_stroll,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)