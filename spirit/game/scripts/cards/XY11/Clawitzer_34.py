from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_special_energy


def _is_mega(p):
    return "MEGA" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def _mega_boost_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and any(is_special_energy(c) for c in hand.children)) and \
        any(_is_mega(p) for p in board.pokemon_in_play(player_id))


async def _mega_boost(ctx):
    """Attach a Special Energy card from your hand to 1 of your Mega Evolution Pokemon."""
    pool = [c for c in ctx.hand() if is_special_energy(c)]
    megas = [p for p in ctx.my_pokemon_in_play() if _is_mega(p)]
    if not pool or not megas:
        return
    e = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Special Energy card")
    t = megas[0] if len(megas) == 1 else await ctx.choose_pokemon(megas, "Attach it to which Mega Evolution Pokémon?")
    if e and t is not None:
        await ctx.attach_energy(e[0], t)


card = PokemonCardDef(
    guid="ccf89052-914a-5c3b-83a0-db58f61bb20c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Ability(
            title="Mega Boost",
            game_text="Once during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Mega Evolution Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_mega_boost_condition,
            effect=_mega_boost,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)