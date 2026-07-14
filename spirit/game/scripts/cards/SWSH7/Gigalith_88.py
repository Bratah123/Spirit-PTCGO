from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import damage_counters_on


async def pressure_shot(ctx):
    """180. This Pokemon also does 10 damage to itself for each damage
    counter on it."""
    await ctx.deal_damage()
    counters = damage_counters_on("self")(ctx)
    if counters:
        await ctx.deal_damage(counters * 10, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="e4f64fa3-e6fe-5828-9ef9-c0e8d6bfff72",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=protect_next_turn(reduce=50),
        ),
        Attack(
            title="Pressure Shot",
            game_text="This Pok\u00e9mon also does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=pressure_shot,
        ),
    ],
)