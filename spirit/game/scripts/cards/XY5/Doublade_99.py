from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _false_swipe(ctx):
    """Flip: heads, put damage counters on the opponent's Active until its HP is 10."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    d = ctx.defender
    if not (results and results[0]) or d is None:
        return
    hp = d.get_attribute(AttrID.HP, 0)
    if hp > 10:
        await ctx.deal_damage(hp - 10, target=d, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="df30da94-95e3-5827-8011-fc88a7c64315",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="False Swipe",
            game_text="Flip a coin. If heads, put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_false_swipe,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)