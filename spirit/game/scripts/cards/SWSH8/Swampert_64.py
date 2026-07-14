from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.support_common import requires_hand


def _is_water_or_fighting_energy(card):
    return (energy_provides_type(card, PokemonTypes.WATER.value)
            or energy_provides_type(card, PokemonTypes.FIGHTING.value))


async def muddy_maker(ctx):
    """Once per turn, you may attach a Water or Fighting Energy card from
    your hand to 1 of your Pokemon."""
    if not await ctx.ask_yes_no(
        "Attach a Water Energy card or a Fighting Energy card from your hand to 1 of your Pokémon?"
    ):
        return
    energies = [c for c in ctx.hand() if _is_water_or_fighting_energy(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose a Water or Fighting Energy card to attach.")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach the Energy to.")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="1a6726ed-c32d-586d-bc40-3719f4603ea9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Muddy Maker",
            game_text="Once during your turn, you may attach a Water Energy card or a Fighting Energy card from your hand to 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(_is_water_or_fighting_energy),
            effect=muddy_maker,
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=spread_damage(20, side="mine", also_base=True),
        ),
    ],
)