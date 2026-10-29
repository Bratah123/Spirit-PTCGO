from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _discharge(ctx):
    """Discard all Lightning Energy from this Pokemon; 30 per card discarded."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning_energy,
        prompt="Discard all Lightning Energy from this Pokémon")
    await ctx.deal_damage(30 * len(discarded))


card = PokemonCardDef(
    guid="c4ea0092-32e1-5868-a12d-5e239f99005e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic", "Togedemaru"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=777,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon. This attack does 30 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            effect=_discharge,
        ),
    ],
)