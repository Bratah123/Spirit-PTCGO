from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _relaxing_fragrance(ctx):
    """Heal 30 damage and remove all Special Conditions from this Pokemon."""
    await ctx.heal(30, ctx.attacker)
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="c90dd2cb-ba11-5264-9aa8-d28c733d48ee",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=315,
    abilities=[
        Attack(
            title="Double Whip",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(2, per_heads=10),
        ),
        Attack(
            title="Relaxing Fragrance",
            game_text="Heal 30 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_relaxing_fragrance,
        ),
    ],
)