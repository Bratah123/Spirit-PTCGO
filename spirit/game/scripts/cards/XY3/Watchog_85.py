"""STUB: effect not implemented — do not guess mechanics.
Watchog (XY3 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _power_pinch(ctx):
    """Flip 2 coins. For each heads, discard an Energy from the Defending Pokémon."""
    results = await ctx.flip_coins(2, "Power Pinch")
    heads = sum(1 for r in results if r)
    defender = ctx.defender
    if not heads or defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, heads, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="7474be87-192e-5644-bada-e780a5c1411b",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Watchog"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Held-Item Inspection",
            game_text="Your opponent reveals his or her hand. Choose an Item card you find there. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Thorough Crunch",
            game_text="Flip 2 coins. For each heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=_power_pinch,
        ),
    ],
)