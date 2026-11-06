from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


async def _heart_wink(ctx):
    """Flip a coin. If heads, your opponent can't draw a card at the
    beginning of their next turn."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        ctx.session.skip_turn_draw.add(
            (ctx.opponent_id, ctx.session.turn_state.turn_number + 1))


card = PokemonCardDef(
    guid="81353754-84ab-5142-b7bd-ae0303a7842b",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=370,
    abilities=[
        Attack(
            title="Heart Wink",
            game_text="Flip a coin. If heads, your opponent can't draw a card at the beginning of his or her next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_heart_wink,
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_attack(1),
        ),
    ],
)