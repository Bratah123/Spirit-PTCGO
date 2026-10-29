from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _rushing_water(ctx):
    """40; move an Energy from the opponent's Active to 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if d is None or not bench or not ctx.attached_energies(d) or ctx.effects_blocked(d):
        return
    await ctx.move_energy_freely([d], bench, max_count=1, prompt="Move an Energy to which Benched Pokémon?")


card = PokemonCardDef(
    guid="a28d05a5-6e9e-5217-b72c-a7655c5f0ee0",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Struggle Bug",
            game_text="Move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_rushing_water,
        ),
    ],
)