from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks, snipe_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


_snipe = snipe_attack(20, count=2, also_base=True)


async def _burning_icicles(ctx):
    """40; with any Fire Energy attached, 20 to 2 of your opponent's Benched Pokemon."""
    if any(_is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        await _snipe(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="fbfbe142-d21a-51cb-8ca8-4afbddb5a21e",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name",
    display_name="White Kyurem",
    searchable_by=["White Kyurem", "Basic", "WhiteKyurem"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Burning Icicles",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, this attack does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_burning_icicles,
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_freeze_shock,
        ),
    ],
)