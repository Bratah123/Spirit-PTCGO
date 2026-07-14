from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench


async def max_lance(ctx):
    """You may discard up to 2 Energy from this Pokémon: +120 damage each."""
    discarded = []
    if ctx.attached_energies(ctx.attacker) and await ctx.ask_yes_no(
            "Discard up to 2 Energy from this Pokémon?"):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 2, minimum=0,
            prompt="Choose up to 2 Energy to discard")
    await ctx.deal_damage(10 + 120 * len(discarded))


card = PokemonCardDef(
    guid="ddb00149-826c-5fa4-bea2-258d68acd9e6",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexVMAX.Name",
    display_name="Ice Rider Calyrex VMAX",
    searchable_by=["Ice Rider Calyrex VMAX", "VMAX", "IceRiderCalyrexVMAX"],
    subtypes=["VMAX"],
    collector_number=202,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    family_id=898,
    abilities=[
        Attack(
            title="Ride of the High King",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 30, base=10),
        ),
        Attack(
            title="Max Lance",
            game_text="You may discard up to 2 Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            damage_operator="+",
            effect=max_lance,
        ),
    ],
)