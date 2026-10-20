from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _shuriken_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return pokemon is not None and pokemon is board.active_pokemon(player_id) and bool(hand) \
        and any(is_energy_card(c) and _is_water_energy(c) for c in hand.children)


async def _giant_water_shuriken(ctx):
    """If Active, discard a Water Energy card from your hand: 6 damage counters on 1 of your opponent's Pokemon."""
    pool = [c for c in ctx.hand() if is_energy_card(c) and _is_water_energy(c)]
    if not pool:
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard a Water Energy card")
    if not pick:
        return
    await ctx.discard_cards(pick)
    opp = ctx.opponent_pokemon_in_play()
    target = opp[0] if len(opp) == 1 else await ctx.choose_pokemon(opp, "Put 6 damage counters on which Pokémon?")
    if target is not None:
        await ctx.place_damage_counters(6, [target])


card = PokemonCardDef(
    guid="524342c2-6ed5-5564-8a1c-99790c2209e4",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaBREAK.Name",
    display_name="Greninja BREAK",
    searchable_by=["Greninja BREAK", "BREAK", "GreninjaBREAK"],
    subtypes=["BREAK"],
    collector_number=41,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Giant Water Shuriken",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may discard a Water Energy card from your hand. If you do, put 6 damage counters on 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_shuriken_condition,
            effect=_giant_water_shuriken,
        ),
    ],
)