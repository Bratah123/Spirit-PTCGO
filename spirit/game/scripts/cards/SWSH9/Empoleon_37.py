from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.constants import BENCH_CAPACITY


def emergency_surfacing_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if hand and hand.children:
        return False
    bench = board.find_player_area(player_id, "bench")
    return bench is not None and BENCH_CAPACITY - len(bench.children) >= 1


async def emergency_surfacing(ctx):
    """Once per turn, from the discard pile with an empty hand: you may put
    this Pokémon onto your Bench. If you do, draw 3 cards."""
    if not await ctx.ask_yes_no(
        "Put Empoleon onto your Bench? If you do, draw 3 cards."
    ):
        return
    if await ctx.bench_pokemon(ctx.source):
        await ctx.draw_cards(3)

card = PokemonCardDef(
    guid="9a89e800-00ef-5265-9849-189dd799d42c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Emergency Surfacing",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile and you have no cards in your hand, you may put this Pok\u00e9mon onto your Bench. If you do, draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            condition=emergency_surfacing_condition,
            effect=emergency_surfacing,
        ),
        Attack(
            title="Water Arrow",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(60, pool="any", count=1),
        ),
    ],
)