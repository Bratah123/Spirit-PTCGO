from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


_STING = condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, counters=4)


async def _hazard_stinger(ctx):
    """40; discard all Energy from this Pokemon; the opponent's Active is
    Paralyzed and Poisoned (4 counters between turns)."""
    await _STING(ctx)
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.discard_cards(energies)


card = PokemonCardDef(
    guid="3d5f1a5b-d016-5c03-b005-2eb98b746e31",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBeedrillEX.Name",
    display_name="M Beedrill-EX",
    searchable_by=["M Beedrill-EX", "MEGA", "EX", "MBeedrillEX"],
    subtypes=["MEGA", "EX"],
    collector_number=158,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name",
    family_id=15,
    abilities=[
        Attack(
            title="Hazard Stinger",
            game_text="Discard all Energy attached to this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned. Put 4 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            effect=_hazard_stinger,
        ),
    ],
)