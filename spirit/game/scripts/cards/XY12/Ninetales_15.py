from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def _lure(ctx):
    """Switch 1 of the opponent's Benched Pokemon with their Active; the new
    Active can't retreat during the opponent's next turn."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    t = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if t is not None and await ctx.switch_active(ctx.opponent_id, t):
        if not ctx.effects_blocked(t):
            ctx.lock_retreat(t)


card = PokemonCardDef(
    guid="f2416f30-bac8-5288-98fd-50bd4987972f",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Lure",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. The new Active Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1},
            effect=_lure,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)