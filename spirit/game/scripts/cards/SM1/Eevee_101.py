from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.attributes import AttrID
from spirit.game.content.definitions import evolves_from_chain
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


async def _energy_evolution(ctx):
    """Attaching a basic Energy from hand to this Pokemon on your turn: you may
    search for a card that evolves from it of that Energy's type and evolve."""
    energy = getattr(ctx, "attached_energy", None)
    if ctx.energy_receiver is not ctx.source or ctx.attaching_player_id != ctx.player_id:
        return
    if energy is None or not is_basic_energy_card(energy):
        return
    if ctx.session.turn_state.active_player_id != ctx.player_id:
        return

    def _matches(card):
        chain = evolves_from_chain(card.archetype_id)
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        return bool(chain) and chain[0] == "Eevee" and \
            any(energy_provides_type(energy, t) for t in types)

    if not await ctx.ask_yes_no(
            "Search your deck for a card that evolves from Eevee of that Energy's type?"):
        return
    picks = await ctx.search_deck(_matches, count=1, minimum=0,
                                  prompt="Choose a card that evolves from Eevee.")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


async def _quick_draw(ctx):
    """Flip a coin. If heads, draw a card."""
    results = await ctx.flip_coins(1, "Quick Draw")
    if results and results[0]:
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="d2561682-2ff0-5e10-9930-6bf08193954c",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Energy Evolution",
            game_text="When you attach a basic Energy card from your hand to this Pok\u00e9mon during your turn, you may search your deck for a card that evolves from this Pok\u00e9mon that is the same type as that Energy card and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_energy_evolution,
        ),
        Attack(
            title="Quick Draw",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_quick_draw,
        ),
    ],
)