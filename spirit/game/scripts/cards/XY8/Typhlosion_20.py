"""STUB: effect not implemented — do not guess mechanics.
Typhlosion (XY8 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _jagged_fang(ctx):
    """100; discard an Energy from this Pokemon, then one from the opponent's Active."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(ctx.attacker, 1, minimum=1, prompt="Discard an Energy from this Pokémon")
    d = ctx.defender
    if d is not None and ctx.attached_energies(d) and not ctx.effects_blocked(d):
        await ctx.discard_energy_from(d, 1, minimum=1, prompt="Discard an Energy from the Defending Pokémon")


card = PokemonCardDef(
    guid="5d4709c1-33b1-512e-b34c-c48ab8dea9e7",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Massive Eruption",
            game_text="Discard the top 5 cards of your deck. This attack does 80 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flare Destroy",
            game_text="Discard an Energy attached to this Pok\u00e9mon. Then, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=_jagged_fang,
        ),
    ],
)