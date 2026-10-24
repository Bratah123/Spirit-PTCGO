from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.effects import is_plasma_energy
from spirit.game.card_effects.attacks_common import snipe_attack


async def _red_signal(ctx):
    """When you attach a Plasma Energy from your hand to this Pokemon, you may
    switch 1 of your opponent's Benched Pokemon with their Active Pokemon."""
    if (getattr(ctx, "energy_receiver", None) is not ctx.source
            or getattr(ctx, "attaching_player_id", None) != ctx.player_id
            or not is_plasma_energy(getattr(ctx, "attached_energy", None))):
        return
    bench = ctx.opponent_bench()
    if not bench or not await ctx.ask_yes_no("Use Red Signal to switch your opponent's Active Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose your opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="501e6a72-3eff-500c-b5f4-7d5b8c03d3a4",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "Team Plasma", "GenesectEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=97,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Red Signal",
            game_text="When you attach a Plasma Energy from your hand to this Pok\u00e9mon, you may switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_red_signal,
        ),
        Attack(
            title="Megalo Cannon",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=snipe_attack(20, pool='bench', also_base=True),
        ),
    ],
)