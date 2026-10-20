from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _mystical_fire_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return len(hand.children if hand else []) < 6 and bool(deck and deck.children)


async def _mystical_fire(ctx):
    """Once during your turn, draw cards until you have 6 cards in your hand."""
    await ctx.draw_until(6)


card = PokemonCardDef(
    guid="c4bd9366-b4d4-5a31-b53f-287bac195dfd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Mystical Fire",
            game_text="Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_mystical_fire_condition,
            effect=_mystical_fire,
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.FIRE), 20, base=50),
        ),
    ],
)