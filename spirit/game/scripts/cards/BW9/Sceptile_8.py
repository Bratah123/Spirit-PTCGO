from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _energy_bloom(ctx):
    """Printed damage; heal 20 from each of your Pokemon with any Energy attached."""
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        if ctx.attached_energies(p):
            await ctx.heal(20, p)


card = PokemonCardDef(
    guid="bf4cbda9-7d96-5de9-b232-b25855841290",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
        Attack(
            title="Energy Bloom",
            game_text="Heal 20 damage from each of your Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_energy_bloom,
        ),
    ],
)