from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def sheer_cold(ctx):
    """50 damage. The Defending Pokémon can't attack during your opponent's next turn."""
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


async def icicle_crash(ctx):
    """80 damage. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="d2e81213-884a-5faf-869c-f299128fe61b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1", "Beartic"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Sheer Cold",
            game_text="The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=sheer_cold,
        ),
        Attack(
            title="Icicle Crash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=icicle_crash,
        ),
    ],
)
