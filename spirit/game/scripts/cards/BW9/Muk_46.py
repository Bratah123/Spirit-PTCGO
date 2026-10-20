from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _has(pokemon, condition):
    return CLIENT_SPECIAL_CONDITION_NAMES[condition] in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def _poison_suction(ctx):
    """Printed damage; if the Defending Pokemon is Poisoned, heal 60 from this Pokemon."""
    poisoned = ctx.defender is not None and _has(ctx.defender, SpecialConditions.POISONED)
    await ctx.deal_damage()
    if poisoned:
        await ctx.heal(60, ctx.attacker)


async def _sludge_crash(ctx):
    """Printed damage; flip until tails, discard an Energy from the Defending
    Pokemon for each heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    d = ctx.defender
    if heads and d is not None and not ctx.effects_blocked(d):
        n = min(heads, len(ctx.attached_energies(d)))
        if n:
            await ctx.discard_energy_from(d, n, minimum=n)


card = PokemonCardDef(
    guid="dfd63c0d-5216-5176-9686-923779e05808",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Team Plasma", "Muk"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=46,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Poison Suction",
            game_text="If the Defending Pok\u00e9mon is Poisoned, heal 60 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_poison_suction,
        ),
        Attack(
            title="Sludge Crash",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_sludge_crash,
        ),
    ],
)