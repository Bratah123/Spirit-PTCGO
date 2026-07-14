from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _named(card, name):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == name


async def ball_search(ctx):
    """On play: may put a Poké Ball, a Great Ball, or 1 of each from your
    discard pile into your hand."""
    discard = ctx.discard_pile()
    poke_balls = [c for c in discard if _named(c, "Poké Ball")]
    great_balls = [c for c in discard if _named(c, "Great Ball")]
    if not poke_balls and not great_balls:
        return
    options = []
    if poke_balls:
        options.append(("Poké Ball", poke_balls[:1]))
    if great_balls:
        options.append(("Great Ball", great_balls[:1]))
    if poke_balls and great_balls:
        options.append(("1 of each", poke_balls[:1] + great_balls[:1]))
    if not await ctx.ask_yes_no(
        "Put a Poké Ball, a Great Ball, or 1 of each from your discard pile into your hand?"
    ):
        return
    if len(options) == 1:
        idx = 0
    else:
        idx = await ctx.choose(
            "Choose which to put into your hand.", [label for label, _ in options]
        )
    await ctx.put_in_hand(options[idx][1], reveal=False)


card = PokemonCardDef(
    guid="bc46f911-8081-5ffe-a712-08b5fcc2d194",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic", "Yamper"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Ability(
            title="Ball Search",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Pok\u00e9 Ball card, a Great Ball card, or 1 of each from your discard pile into your hand.",
            trigger=Triggers.ON_PLAY,
            effect=ball_search,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)