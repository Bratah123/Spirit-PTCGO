from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _energy_bomb(ctx):
    """70; you may move all Energy from this Pokemon to your Benched Pokemon in any way."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attached_energies(ctx.attacker) and await ctx.ask_yes_no("Move Energy to your Benched Pokémon?"):
        await ctx.move_energy_freely([ctx.attacker], bench, prompt="Choose an Energy to move")


card = PokemonCardDef(
    guid="829b611a-a7a2-5bd2-973d-54763ea3c983",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Continuous Tumble",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
        Attack(
            title="Energy Bomb",
            game_text="You may move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_energy_bomb,
        ),
    ],
)