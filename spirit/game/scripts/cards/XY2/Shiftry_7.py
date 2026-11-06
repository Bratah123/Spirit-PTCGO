from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _leaf_draw_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_grass_energy_card(c) for c in hand.children)


async def _leaf_draw(ctx):
    """Discard a Grass Energy card from your hand. If you do, draw 3 cards."""
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_is_grass_energy_card,
                                         prompt="Discard a Grass Energy card")
    if picked:
        await ctx.draw_cards(3)


async def _deranged_dance(ctx):
    """20 times the number of Benched Pokemon (both players)."""
    await ctx.deal_damage(20 * (len(ctx.my_bench()) + len(ctx.opponent_bench())))


card = PokemonCardDef(
    guid="9a2fe570-6e11-58ef-b037-ebc2b0e7d053",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Leaf Draw",
            game_text="Once during your turn (before your attack), you may discard a Grass Energy card from your hand. If you do, draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_leaf_draw_condition,
            effect=_leaf_draw,
        ),
        Attack(
            title="Deranged Dance",
            game_text="This attack does 20 damage times the number of Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=_deranged_dance,
        ),
    ],
)