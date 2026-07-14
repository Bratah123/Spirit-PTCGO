from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.pokemon import energy_provides_type, in_active_spot
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_clefairy(pokemon) -> bool:
    d = def_for(pokemon.archetype_id)
    return bool(d) and d.display_name == "Clefairy"


def _has_benched_clefairy(board, player_id) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(_is_clefairy(c) for c in bench.children)


def moon_watching_party_condition(board, player_id, pokemon):
    return in_active_spot(board, player_id, pokemon) and \
        _has_benched_clefairy(board, player_id)


async def moon_watching_party(ctx):
    """Once per turn, in the Active Spot: for each Benched Clefairy, you may
    search a Psychic Energy card and attach it to that Clefairy."""
    targets = [p for p in ctx.my_bench() if _is_clefairy(p)]
    if not targets:
        return
    searched_any = False
    for target in targets:
        if not await ctx.ask_yes_no(
                "Search your deck for a Psychic Energy card to attach to your Benched Clefairy?"):
            continue
        picks = await ctx.search_deck(
            lambda c: energy_provides_type(c, PokemonTypes.PSYCHIC.value),
            count=1, minimum=0,
            prompt="Choose a Psychic Energy card to attach.",
        )
        if picks:
            await ctx.attach_energy(picks[0], target)
        searched_any = True
    if searched_any:
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="77c480af-bb9a-5b71-b32f-41a2c325236e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=35,
    abilities=[
        Ability(
            title="Moon-Watching Party",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, for each of your Benched Clefairy, you may search your deck for a Psychic Energy card and attach it to that Clefairy. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=moon_watching_party_condition,
            effect=moon_watching_party,
        ),
        Attack(
            title="Wonder Storm",
            game_text="This attack does 20 damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(
                count_energy("mine", energy_type=PokemonTypes.PSYCHIC), 20,
            ),
        ),
    ],
)