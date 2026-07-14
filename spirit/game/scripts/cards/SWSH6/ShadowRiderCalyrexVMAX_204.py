from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import energy_provides_type


def _is_psychic_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.PSYCHIC.value)


def _is_psychic_pokemon(pokemon) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value in types


def underworld_door_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if not bench or not any(_is_psychic_pokemon(p) for p in bench.children):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_psychic_energy(c) for c in hand.children)


async def underworld_door(ctx):
    """You may attach a Psychic Energy from hand to a Benched Psychic
    Pokemon. If you did, draw 2 cards."""
    bench = [p for p in ctx.my_bench() if _is_psychic_pokemon(p)]
    energies = [c for c in ctx.hand() if _is_psychic_energy(c)]
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no(
            "Attach a Psychic Energy card from your hand to 1 of your "
            "Benched Psychic Pokémon?"):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Psychic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the Benched Psychic Pokémon to attach it to"
    )
    if target is None:
        return
    await ctx.attach_energy(picked[0], target)
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="6ed1b3e8-c46e-5abd-8941-8efe6dab32e7",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexVMAX.Name",
    display_name="Shadow Rider Calyrex VMAX",
    searchable_by=["Shadow Rider Calyrex VMAX", "VMAX", "ShadowRiderCalyrexVMAX"],
    subtypes=["VMAX"],
    collector_number=204,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    family_id=898,
    abilities=[
        Ability(
            title="Underworld Door",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Benched Psychic Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=underworld_door_condition,
            effect=underworld_door,
        ),
        Attack(
            title="Max Geist",
            game_text="This attack does 30 more damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.PSYCHIC), 30, base=10),
        ),
    ],
)