from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_rapid_strike(card) -> bool:
    return "Rapid Strike" in subtypes_for(card.archetype_id)


async def rapid_strike_search(ctx):
    picks = await ctx.search_deck(
        _is_rapid_strike, count=1, minimum=0,
        prompt="Choose a Rapid Strike card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="31ac23cb-0844-5086-ae10-9c19b57cc367",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Rapid Strike", "Octillery"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=37,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Rapid Strike Search",
            game_text="Once during your turn, you may search your deck for a Rapid Strike card, reveal it, and put it into your hand. Then, shuffle your deck. You can't use more than 1 Rapid Strike Search Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Rapid Strike Search",
            effect=rapid_strike_search,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)