from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


async def _energy_evolution(ctx):
    """When you attach a basic Energy card to this Pokemon: you may search
    your deck for its evolution of that Energy's type and evolve it."""
    energy = getattr(ctx, "attached_energy", None)
    if (getattr(ctx, "attaching_player_id", None) != ctx.player_id
            or getattr(ctx, "energy_receiver", None) is not ctx.source
            or energy is None or not is_basic_energy_card(energy)):
        return
    name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def _fits(c):
        if not name or c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) != name:
            return False
        return any(energy_provides_type(energy, t)
                   for t in (c.get_attribute(AttrID.POKEMON_TYPES) or []))

    if not await ctx.ask_yes_no("Search your deck for an evolution of that Energy's type?"):
        return
    picks = await ctx.search_deck(_fits, count=1, minimum=0,
                                  prompt="Choose a card that evolves from this Pokémon")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ab3b9509-1ba0-519c-98bb-4b70a37d19cf",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Energy Evolution",
            game_text="When you attach a basic Energy card from your hand to this Pok\u00e9mon, you may search your deck for a card that evolves from this Pok\u00e9mon that is the same type as that Energy card and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_energy_evolution,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)