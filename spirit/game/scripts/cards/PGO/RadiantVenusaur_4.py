from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _sunny_bloom_ready(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and hand is not None \
        and len(hand.children) < 4


async def sunny_bloom(ctx):
    """End of your turn: you may draw until you have 4 cards in your hand."""
    if not _sunny_bloom_ready(ctx.board, ctx.player_id, ctx.source):
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no("Use Sunny Bloom? Draw cards until you have "
                                "4 cards in your hand."):
        ctx.suppress_announce = True
        return
    await ctx.draw_until(4)

card = PokemonCardDef(
    guid="2baf28dd-fef2-52c9-826b-1fbf5017d922",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantVenusaur.Name",
    display_name="Radiant Venusaur",
    searchable_by=["Radiant Venusaur", "Basic", "Radiant", "RadiantVenusaur"],
    subtypes=["Basic", "Radiant"],
    collector_number=4,
    set_code="PGO",
    rarity=Rarities.RareRadiant,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Ability(
            title="Sunny Bloom",
            game_text="Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 4 cards in your hand.",
            trigger=Triggers.END_OF_TURN,
            condition=_sunny_bloom_ready,
            effect=sunny_bloom,
        ),
        Attack(
            title="Pollen Hazard",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED,
                                    SpecialConditions.POISONED),
        ),
    ],
)