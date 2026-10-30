from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets


async def _magical_leaf(ctx):
    """20+; heads: +20 and heal 20 from this Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    heads = bool(results and results[0])
    await ctx.deal_damage(ctx.ability.damage + (20 if heads else 0))
    if heads:
        await ctx.heal(20, ctx.attacker)


card = PokemonCardDef(
    guid="5fd52bfd-e398-5360-974a-069512cc18af",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1", "Floette"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    family_id=669,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=heal_targets(30, 'each_own'),
        ),
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 20 more damage and heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2},
            damage=20,
            damage_operator="+",
            effect=_magical_leaf,
        ),
    ],
)