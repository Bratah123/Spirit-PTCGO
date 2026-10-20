from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _ambush_bite(ctx):
    """Flip a coin. If heads, this attack does 20 more damage and discard an
    Energy attached to the Defending Pokemon."""
    heads = (await ctx.flip_coins(1, "Ambush Bite"))[0]
    await ctx.deal_damage(ctx.ability.damage + (20 if heads else 0))
    d = ctx.defender
    if heads and d is not None and not ctx.effects_blocked(d) and ctx.attached_energies(d):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="66c3933a-3ebc-5448-996a-ddd1718a1a51",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title="Ambush Bite",
            game_text="Flip a coin. If heads, this attack does 20 more damage and discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=_ambush_bite,
        ),
    ],
)