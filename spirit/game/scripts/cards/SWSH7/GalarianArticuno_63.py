from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import is_energy_card


def _is_psychic_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.PSYCHIC.value in types


async def cruel_charge(ctx):
    """On play: you may attach up to 2 Psychic Energy cards from your hand
    to this Pokemon."""
    energies = [c for c in ctx.hand() if _is_psychic_energy(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Psychic Energy cards to attach",
    )
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


async def psylaser(ctx):
    """Discard all Psychic Energy from this Pokemon. This attack does 120
    damage to 1 of your opponent's Pokemon. (Don't apply Weakness and
    Resistance for Benched Pokemon.)"""
    await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_psychic_energy,
        prompt="Discard all Psychic Energy from Galarian Articuno",
    )
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(),
        "Choose 1 of your opponent's Pokémon to take 120 damage",
    )
    if target is not None:
        await ctx.deal_damage(120, target=target)


card = PokemonCardDef(
    guid="013aa082-f0ea-5824-a357-4f63b661ecb9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticuno.Name",
    display_name="Galarian Articuno",
    searchable_by=["Galarian Articuno", "Basic", "GalarianArticuno"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Cruel Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Psychic Energy cards from your hand to this Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=cruel_charge,
        ),
        Attack(
            title="Psylaser",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=psylaser,
        ),
    ],
)