from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_lightning_energy


async def electron_crush(ctx):
    """100 damage; you may discard 3 Lightning Energy from this Pokémon for +120."""
    amount = 100
    if await ctx.ask_yes_no("Discard 3 Lightning Energy from this Pokémon?"):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 3, predicate=is_lightning_energy,
            prompt="Discard 3 Lightning Energy",
        )
        if discarded:
            amount += 120
    await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="995b9e25-6841-56e5-b827-e6521eb1944c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Electron Crush",
            game_text="You may discard 3 Lightning Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=electron_crush,
        ),
    ],
)