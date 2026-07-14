from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import is_energy_card


def _is_water_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


def pump_shot_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_water_energy(c) for c in hand.children):
        return False
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    bench = board.find_player_area(opponent, "bench")
    return bool(bench) and len(bench.children) > 0


async def pump_shot(ctx):
    """Discard a Water Energy from hand; put 2 damage counters on 1 of your opponent's Benched Pokemon."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_water_energy,
        prompt="Discard a Water Energy card to use Pump Shot",
    )
    if not discarded:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(20, target=target, as_counters=True)


card = PokemonCardDef(
    guid="76360f77-185a-5c93-9e8e-b9cc93cc38e9",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantBlastoise.Name",
    display_name="Radiant Blastoise",
    searchable_by=["Radiant Blastoise", "Basic", "Radiant", "RadiantBlastoise"],
    subtypes=["Basic", "Radiant"],
    collector_number=18,
    set_code="PGO",
    rarity=Rarities.RareRadiant,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=9,
    abilities=[
        Ability(
            title="Pump Shot",
            game_text="You must discard a Water Energy card from your hand in order to use this Ability. Once during your turn, you may put 2 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=pump_shot_condition,
            effect=pump_shot,
        ),
        Attack(
            title="Torrential Cannon",
            game_text="During your next turn, this Pok\u00e9mon can't use Torrential Cannon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            locks_next_turn=True,
        ),
    ],
)