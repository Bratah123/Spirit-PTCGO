"""STUB: effect not implemented — do not guess mechanics.
Rayquaza-EX (Promo_XY #XY69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _fire_spin(ctx):
    """Printed damage. Flip a coin. If tails, discard 2 Energy from this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Fire Spin")
    if results and not results[0]:
        await ctx.discard_energy_from(ctx.attacker, 2)


card = PokemonCardDef(
    guid="358f08f9-0e90-55ff-82f8-5a660f896fc9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=69,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title="Mega Ascension",
            game_text="Search your deck for M Rayquaza-EX, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aeroscream",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            # STUB: attack effect not implemented
            effect=_fire_spin,
        ),
    ],
)