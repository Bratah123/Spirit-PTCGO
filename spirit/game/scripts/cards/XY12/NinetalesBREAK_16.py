from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _explosive_fireball(ctx):
    """Discard all Fire Energy attached to this Pokemon; 10 + 60 per card discarded."""
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _is_fire_energy(e)]
    if pool:
        await ctx.discard_cards(pool)
    await ctx.deal_damage(10 + 60 * len(pool))


card = PokemonCardDef(
    guid="814beafe-cdef-521d-9272-bfb73b281127",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesBREAK.Name",
    display_name="Ninetales BREAK",
    searchable_by=["Ninetales BREAK", "BREAK", "NinetalesBREAK"],
    subtypes=["BREAK"],
    collector_number=16,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Explosive Fireball",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon. This attack does 60 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=_explosive_fireball,
        ),
    ],
)