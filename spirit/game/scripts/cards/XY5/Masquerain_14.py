from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def _spiral_gyration(ctx):
    """The opponent's Active is Confused; switch this Pokemon with 1 of your Benched."""
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    bench = ctx.my_bench()
    if bench:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="cd799952-d118-5156-b9df-f4076dee6a2f",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Spiral Gyration",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_spiral_gyration,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)