from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _playful(ctx):
    """Flip a coin. If heads, 20 damage times the number of damage counters on this Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        n = damage_counters_on('self')(ctx)
        if n:
            await ctx.deal_damage(20 * n)


card = PokemonCardDef(
    guid="4bf9341a-4a67-5618-b9a7-0e17b6b9e5d2",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Playful",
            game_text="Flip a coin. If heads, this attack does 20 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=_playful,
        ),
    ],
)