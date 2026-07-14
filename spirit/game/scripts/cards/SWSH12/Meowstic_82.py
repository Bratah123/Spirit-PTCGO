from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card


async def inviting_ears(ctx):
    """When played to evolve during your turn, you may search your deck for
    up to 2 Supporter cards, reveal them, put them into your hand, shuffle."""
    if not await ctx.ask_yes_no("Search your deck for up to 2 Supporter cards?"):
        return
    picks = await ctx.search_deck(
        is_supporter_card, count=2, minimum=0,
        prompt="Choose up to 2 Supporter cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9987c931-7cb2-558d-9509-67055957e9a6",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Ability(
            title="Inviting Ears",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 2 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=inviting_ears,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)