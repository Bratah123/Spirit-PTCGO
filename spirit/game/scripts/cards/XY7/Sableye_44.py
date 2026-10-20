from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import place_counters


async def _bewitching_eyes(ctx):
    """Choose a Supporter card from your opponent's discard pile and use it as
    the effect of this attack."""
    pool = [c for c in ctx.discard_pile(ctx.opponent_id) if is_supporter_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter to use")
    definition = def_for(picks[0].archetype_id) if picks else None
    effect = getattr(definition, "effect", None)
    if effect is None:
        return
    condition = getattr(definition, "condition", None)
    try:
        if condition is not None and not condition(ctx.board, ctx.player_id):
            return
    except TypeError:
        pass
    await effect(ctx)


card = PokemonCardDef(
    guid="2e9af8ac-c023-5caa-a614-6d33d7d4220b",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title="Bewitching Eyes",
            game_text="Choose a Supporter card from your opponent's discard pile and use it as the effect of this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_bewitching_eyes,
        ),
        Attack(
            title="Furtive Drop",
            game_text="Put 3 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(3),
        ),
    ],
)