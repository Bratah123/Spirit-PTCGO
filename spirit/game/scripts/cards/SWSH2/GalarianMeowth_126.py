from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import requires_hand


def _is_galarian_perrserker(card):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Galarian Perrserker"


async def evolution_roar(ctx):
    await ctx.discard_from_hand(2, prompt="Discard 2 cards to use Evolution Roar")
    if await ctx.ask_yes_no("Search your deck for a Galarian Perrserker?"):
        picks = await ctx.search_deck(
            _is_galarian_perrserker, count=1, minimum=0,
            prompt="Choose a Galarian Perrserker to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9c92919b-3dcf-55b8-866f-daa63bc46076",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    display_name="Galarian Meowth",
    searchable_by=["Galarian Meowth", "Basic", "GalarianMeowth"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=52,
    abilities=[
        Ability(
            title="Evolution Roar",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may search your deck for a Galarian Perrserker, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=2),
            effect=evolution_roar,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)