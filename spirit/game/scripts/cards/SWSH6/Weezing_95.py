from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import energy_provides_type


def is_darkness_energy(card):
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)


_attach_darkness_energy = attach_from_discard(
    predicate=is_darkness_energy, count=1, target="self", minimum=1,
    prompt="Choose a Darkness Energy card from your discard pile to attach",
)


async def mixin_toxin(ctx):
    """Opponent's Active is now Confused. Attach a Darkness Energy card from discard to this Pokémon."""
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    await _attach_darkness_energy(ctx)


card = PokemonCardDef(
    guid="665c9743-fdf0-5d83-a2c5-8ff46fd6810e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Mixin' Toxin",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Attach a Darkness Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=mixin_toxin,
        ),
        Attack(
            title="Smog Burst",
            game_text="This attack does 20 more damage for each Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.DARKNESS), 20, base=20),
        ),
    ],
)