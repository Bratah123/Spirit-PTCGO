from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


def _farewell_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return pokemon is not None and bench is not None and pokemon in bench.children


async def _farewell_letter(ctx):
    """Discard this Benched Pokemon and all cards attached (not a Knock Out); draw a card."""
    await ctx.discard_cards(full_stack(ctx.source))
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="3fab86ca-52a6-5664-b8d0-6f2f6f670b27",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="Farewell Letter",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may discard this Pok\u00e9mon and all cards attached to it (this does not count as a Knock Out). If you do, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_farewell_condition,
            effect=_farewell_letter,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)