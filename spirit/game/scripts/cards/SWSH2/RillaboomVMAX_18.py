from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def max_beating(ctx):
    """Discard up to 3 Grass Energy from this Pokemon; +50 damage per card discarded."""
    picks = await ctx.discard_energy_from(
        ctx.attacker, 3, minimum=0,
        predicate=lambda c: energy_provides_type(c, PokemonTypes.GRASS.value),
        prompt="Choose up to 3 Grass Energy to discard from this Pokémon.",
    )
    await ctx.deal_damage(130 + 50 * len(picks))


card = PokemonCardDef(
    guid="f2d5f72b-3b42-5e7d-8876-d3c18c4f3605",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomVMAX.Name",
    display_name="Rillaboom VMAX",
    searchable_by=["Rillaboom VMAX", "VMAX", "RillaboomVMAX"],
    subtypes=["VMAX"],
    collector_number=18,
    set_code="SWSH2",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    family_id=812,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Max Beating",
            game_text="You may discard up to 3 Grass Energy from this Pok\u00e9mon. If you do, this attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=max_beating,
        ),
    ],
)