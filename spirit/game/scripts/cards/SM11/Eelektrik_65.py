from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _discharge(ctx):
    """Discard all Lightning Energy from this Pokemon; 30 per card discarded."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning_energy,
        prompt="Discard all Lightning Energy from this Pokémon")
    await ctx.deal_damage(30 * len(discarded))


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


card = PokemonCardDef(
    guid="a838f627-ec1f-5953-8041-870b7d7fbf7f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Overspark",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon. This attack does 30 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            effect=_discharge,
        ),
    ],
)