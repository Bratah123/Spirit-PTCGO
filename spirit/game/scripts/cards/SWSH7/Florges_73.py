from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _rapid_strike_connection_condition(board, player_id, pokemon):
    in_play = board.pokemon_in_play(player_id)
    if not any("Rapid Strike" in subtypes_for(p.archetype_id) for p in in_play):
        return False
    return any(board.attached_energies(p) for p in in_play)


async def rapid_strike_connection(ctx):
    """As often as you like: move an Energy from 1 of your Pokemon to 1 of
    your Rapid Strike Pokemon."""
    sources = ctx.my_pokemon_in_play()
    dests = [p for p in sources if "Rapid Strike" in subtypes_for(p.archetype_id)]
    if not dests:
        return
    await ctx.move_energy_freely(sources, dests)


card = PokemonCardDef(
    guid="34694ea2-ac3d-5733-9d5f-f68214e3cb52",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2", "Rapid Strike", "Florges"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=73,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Rapid Strike Connection",
            game_text="As often as you like during your turn, you may move an Energy from 1 of your Pokémon to 1 of your Rapid Strike Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_rapid_strike_connection_condition,
            effect=rapid_strike_connection,
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
