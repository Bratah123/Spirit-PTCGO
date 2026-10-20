from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import is_energy


async def shear(ctx):
    """Discard top 5 of your deck; attach any Fighting Energy among them."""
    top = ctx.deck_top(5)
    await ctx.discard_cards(top)
    for card in top:
        if is_energy(card) and energy_provides_type(
                card, PokemonTypes.FIGHTING.value):
            await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="23ef2ef2-9eaf-5118-9b0b-8480c01e74ce",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Shear",
            game_text="Discard the top 5 cards of your deck. If any of those cards are Fighting Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=shear,
        ),
        Attack(
            title="Rock Bullet",
            game_text="Does 20 more damage for each Fighting Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", PokemonTypes.FIGHTING), 20, base=40),
        ),
    ],
)
