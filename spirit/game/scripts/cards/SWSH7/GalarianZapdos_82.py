from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.pokemon import is_energy_card


def _is_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


async def strong_legs_charge(ctx):
    """On play: you may attach up to 2 Fighting Energy cards from your hand
    to this Pokemon."""
    energies = [c for c in ctx.hand() if _is_fighting_energy(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Fighting Energy cards to attach",
    )
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


async def zapper_kick(ctx):
    """70. You may discard all Energy from this Pokemon. If you do, your
    opponent's Active Pokemon is now Paralyzed."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no("Discard all Energy from this Pokémon?"):
        await ctx.discard_energy_from(
            ctx.attacker, 99, prompt="Discard all Energy from Galarian Zapdos"
        )
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="44d1a4de-d325-5bf3-ab01-a81510979fff",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZapdos.Name",
    display_name="Galarian Zapdos",
    searchable_by=["Galarian Zapdos", "Basic", "GalarianZapdos"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=145,
    abilities=[
        Ability(
            title="Strong Legs Charge",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may attach up to 2 Fighting Energy cards from your hand to this Pokémon.",
            trigger=Triggers.ON_PLAY,
            effect=strong_legs_charge,
        ),
        Attack(
            title="Zapper Kick",
            game_text="You may discard all Energy from this Pokémon. If you do, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=zapper_kick,
        ),
    ],
)
