from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _magical_leaf(ctx):
    """Flip a coin. If heads, +30 damage and heal 30 damage from this Pokemon."""
    results = await ctx.flip_coins(1, "Magical Leaf")
    heads = bool(results and results[0])
    await ctx.deal_damage(ctx.ability.damage + (30 if heads else 0))
    if heads:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="b9ccf504-c1f4-59c2-ad73-dba48a960d34",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1", "Leafeon"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Soothing Scent",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 30 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=_magical_leaf,
        ),
    ],
)