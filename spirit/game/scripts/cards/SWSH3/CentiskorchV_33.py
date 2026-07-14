from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def radiating_heat(ctx):
    """20 damage. You may discard an Energy from this Pokémon; if you do,
    discard an Energy from the opponent's Active Pokémon."""
    await ctx.deal_damage()
    if not ctx.attached_energies(ctx.attacker):
        return
    if not await ctx.ask_yes_no("Discard an Energy from this Pokémon?"):
        return
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.defender
    if defender is not None and ctx.attached_energies(defender) \
            and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="90b18e7c-0895-5543-8cd6-7cad97bf8b65",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    display_name="Centiskorch V",
    searchable_by=["Centiskorch V", "Basic", "V", "CentiskorchV"],
    subtypes=["Basic", "V"],
    collector_number=33,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=851,
    abilities=[
        Attack(
            title="Radiating Heat",
            game_text="You may discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=radiating_heat,
        ),
        Attack(
            title="Burning Train",
            cost={PokemonTypes.FIRE: 4},
            damage=180,
        ),
    ],
)
