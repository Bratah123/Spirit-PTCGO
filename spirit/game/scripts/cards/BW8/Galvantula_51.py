from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _discharge(ctx):
    """Discard all Lightning Energy attached to this Pokemon; 30 damage times
    the number of Energy cards discarded."""
    cards = [e for e in ctx.attached_energies(ctx.attacker) if _is_lightning_energy(e)]
    if cards:
        await ctx.discard_cards(cards)
    await ctx.deal_damage(30 * len(cards))


card = PokemonCardDef(
    guid="a3a38847-cfd5-5057-bf85-737a8cd09f43",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            effect=_discharge,
        ),
        Attack(
            title="Signal Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)