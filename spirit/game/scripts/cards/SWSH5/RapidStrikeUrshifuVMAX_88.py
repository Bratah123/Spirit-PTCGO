from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, snipe_attack


async def gmax_rapid_flow(ctx):
    """Discard all Energy from this Pokémon, then 120 to 2 of the opponent's Pokémon (no W/R on Bench)."""
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Choose Energy to discard from this Pokémon"
    )
    await snipe_attack(120, pool="any", count=2)(ctx)


card = PokemonCardDef(
    guid="f732bc5c-f93c-5290-bb63-ca77e024d80a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuVMAX.Name",
    display_name="Rapid Strike Urshifu VMAX",
    searchable_by=["Rapid Strike Urshifu VMAX", "VMAX", "Rapid Strike", "RapidStrikeUrshifuVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=88,
    set_code="SWSH5",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name",
    family_id=892,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.entered_active_this_turn(ctx.attacker), 120),
        ),
        Attack(
            title="G-Max Rapid Flow",
            game_text="Discard all Energy from this Pokémon. This attack does 120 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=gmax_rapid_flow,
        ),
    ],
)
