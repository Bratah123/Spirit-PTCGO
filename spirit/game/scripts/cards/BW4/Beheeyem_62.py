from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _brain_control(ctx):
    """Opponent reveals their hand; put a chosen card on the bottom of their deck."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card to put on the bottom of your opponent's deck.",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="9f890cc8-28c7-503b-b593-6d268ab550cf",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1", "Beheeyem"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Brain Control",
            game_text="Your opponent reveals his or her hand. Choose a card from there and put it on the bottom of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_brain_control,
        ),
        Attack(
            title="Psybeam",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)