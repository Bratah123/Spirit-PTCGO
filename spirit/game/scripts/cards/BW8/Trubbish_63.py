from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.support_common import search_to_hand


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value


_search_tool = search_to_hand(_is_tool, count=1, minimum=0, reveal=True,
                              prompt="Choose a Pokémon Tool card")


async def _pile_up(ctx):
    """Flip a coin. If heads, search your deck for a Pokemon Tool card, reveal
    it and put it into your hand; shuffle."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await _search_tool(ctx)


card = PokemonCardDef(
    guid="57eed303-2a46-56fd-b93e-76fe4698745c",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Pile Up",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon Tool card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_pile_up,
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)