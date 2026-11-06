from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _electric_shock(ctx):
    """70; discard all Lightning Energy from this Pokemon; the opponent's Active is Paralyzed."""
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _is_lightning_energy(e)]
    if pool:
        await ctx.discard_cards(pool)
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="b80b839b-4a92-5fa2-a23a-2ad3ca9d274d",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Lightning Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Electric Shock",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_electric_shock,
        ),
    ],
)