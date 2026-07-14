from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def max_wind_spirit(ctx):
    """120, +120 more if a Stadium is in play; then discard that Stadium."""
    stadium = ctx.stadium_in_play()
    amount = 120 + (120 if stadium is not None else 0)
    await ctx.deal_damage(amount)
    if stadium is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="eb417894-6b67-5be8-bb18-a1694571ef31",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusVMAX.Name",
    display_name="Tornadus VMAX",
    searchable_by=["Tornadus VMAX", "VMAX", "Single Strike", "TornadusVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=125,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusV.Name",
    family_id=641,
    abilities=[
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Max Wind Spirit",
            game_text="If a Stadium is in play, this attack does 120 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=max_wind_spirit,
        ),
    ],
)