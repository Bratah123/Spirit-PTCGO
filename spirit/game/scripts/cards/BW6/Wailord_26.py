from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def _water_cannon(ctx):
    """Flip a coin. If heads, 30 damage times the Water Energy attached to this Pokemon."""
    results = await ctx.flip_coins(1, "Water Cannon")
    if not results or not results[0]:
        return
    water = sum(1 for e in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(e, PokemonTypes.WATER.value))
    if water:
        await ctx.deal_damage(30 * water)


card = PokemonCardDef(
    guid="ef191cce-68f1-520c-9164-5f48e2ede195",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Water Cannon",
            game_text="Flip a coin. If heads, this attack does 30 damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=_water_cannon,
        ),
        Attack(
            title="Giant Wave",
            game_text="This Pok\u00e9mon can't use Giant Wave during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)