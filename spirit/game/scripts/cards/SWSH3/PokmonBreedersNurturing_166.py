from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities


def _breeders_nurturing_condition(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    return turn_state is not None and turn_state.turn_number > 2


async def pokemon_breeders_nurturing(ctx):
    """Choose up to 2 of your Pokemon in play (not put into play this turn);
    for each, search the deck for a card that evolves from it and evolve it."""
    turn_state = ctx.session.turn_state
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if turn_state.entered_play_turn.get(p.entity_id) != turn_state.turn_number
    ]
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Choose up to 2 of your Pokémon in play to evolve.",
    )
    if not targets:
        return
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="08ff5298-b4d9-5bf0-bb0d-00d48987609f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreedersNurturing.Name",
    display_name="PokÃ©mon Breeder's Nurturing",
    searchable_by=["Pok\u00c3\u00a9mon Breeder's Nurturing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=pokemon_breeders_nurturing,
    condition=_breeders_nurturing_condition
)
