from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.pokemon import energy_provides_type


async def shock_bolt(ctx):
    """90 damage. Flip a coin. If tails, discard all Lightning Energy from self."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Shock Bolt")
    if results and not results[0]:
        lightning = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.LIGHTNING.value)
        ]
        if lightning:
            await ctx.discard_cards(lightning)


card = PokemonCardDef(
    guid="d6b4e666-beea-5cae-9965-f1f42d980c62",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Zebstrika"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Shock Bolt",
            game_text="Flip a coin. If tails, discard all Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=shock_bolt,
        ),
    ],
)
