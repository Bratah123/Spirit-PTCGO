from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType


async def metal_reversal(ctx):
    """Optional: switch Defending with a Benched Pokémon, then deal damage."""
    bench = ctx.opponent_bench()
    if bench:
        pick = await ctx.choose_pokemon(
            bench, "You may choose a Benched Pokémon to switch into the Active Spot",
            optional=True,
        )
        if pick:
            await ctx.switch_active(ctx.opponent_id, pick)
    await ctx.deal_damage()

_attack = Attack(
    title="Metal Reversal",
    game_text="Before doing damage, you may choose 1 of your opponent's Benched Pokémon and switch it with the Defending Pokémon.",
    cost={PokemonTypes.METAL: 1},
    damage=10,
    effect=metal_reversal,
    )

card = TrainerCardDef(
    guid="87584bc2-9241-51ed-b3b0-368b1887fa61",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCube01.Name",
    display_name="Metal Cube 01",
    searchable_by=["Metal Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.METAL: pokemon_has_type(p, _t)
