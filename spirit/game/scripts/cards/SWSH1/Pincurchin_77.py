from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def shocking_needles(ctx):
    """Flip 4 coins. 30 damage per heads; 2+ heads also Paralyzes the Defending Pokemon."""
    results = await ctx.flip_coins(4, ctx.ability.title)
    heads = sum(results)
    if heads:
        await ctx.deal_damage(30 * heads)
    if heads >= 2 and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="8fdce931-5d96-51ff-8ee4-a2dd043b9bde",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name",
    display_name="Pincurchin",
    searchable_by=["Pincurchin", "Basic", "Pincurchin"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Attack(
            title="Shocking Needles",
            game_text="Flip 4 coins. This attack does 30 damage for each heads. If at least 2 of them are heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="x",
            effect=shocking_needles,
        ),
    ],
)