from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _nurses_egg(ctx):
    """Heal 100 from each of your Benched Pokemon, then discard 2 Energy from this Pokemon."""
    for p in ctx.my_bench():
        await ctx.heal(100, p)
    n = min(2, len(ctx.attached_energies(ctx.attacker)))
    if n:
        await ctx.discard_energy_from(ctx.attacker, n, minimum=n, prompt="Choose 2 Energy to discard")


card = PokemonCardDef(
    guid="f141acdb-fa93-5a3f-af03-b9b4821c133a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=242,
    abilities=[
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=flip_damage(2, per_heads=40),
        ),
        Attack(
            title="Nurse's Egg",
            game_text="Heal 100 damage from each of your Benched Pok\u00e9mon. Then, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=_nurses_egg,
        ),
    ],
)