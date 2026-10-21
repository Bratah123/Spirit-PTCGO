from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks, bonus_if
from spirit.game.session.effects import is_special_energy


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="43c9ed64-fd7c-504f-87c6-8e5a6dc1e317",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 1", "Tyrantrum"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Chew Up",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached to it, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and any(is_special_energy(e) for e in ctx.attached_energies(ctx.defender)), 90),
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=_freeze_shock,
        ),
    ],
)