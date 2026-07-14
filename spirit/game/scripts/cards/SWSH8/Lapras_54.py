from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def splash_arch(ctx):
    """Put all Energy attached to this Pokémon into your hand. 100 damage to
    1 of your opponent's Benched Pokémon (no W/R)."""
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.put_in_hand(list(energies), reveal=False)
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon"
        )
        if target is not None:
            await ctx.deal_damage(100, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="f3332db4-1d0d-571e-8049-75d336c136a9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Rapid Strike", "Lapras"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=54,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Splash Arch",
            game_text="Put all Energy attached to this Pok\u00e9mon into your hand. This attack does 100 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=splash_arch,
        ),
    ],
)