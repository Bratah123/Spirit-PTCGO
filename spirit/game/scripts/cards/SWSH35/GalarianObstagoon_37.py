from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


def _wicked_ruler_condition(board, player_id, pokemon):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand) and len(hand.children) > 4


async def wicked_ruler(ctx):
    hand = ctx.hand(ctx.opponent_id)
    excess = len(hand) - 4
    if excess <= 0:
        return
    await ctx.discard_from_hand(
        excess, minimum=excess, player_id=ctx.opponent_id,
        prompt="Discard cards until you have 4 cards in your hand.",
    )


async def knuckle_impact(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="fee652b7-2d45-54cc-96af-0de41ccfe985",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Wicked Ruler",
            game_text="Once during your turn, you may have your opponent discard cards from their hand until they have 4 cards in their hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_wicked_ruler_condition,
            effect=wicked_ruler,
        ),
        Attack(
            title="Knuckle Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=knuckle_impact,
        ),
    ],
)