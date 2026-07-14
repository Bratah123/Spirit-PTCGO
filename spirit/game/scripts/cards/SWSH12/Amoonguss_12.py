from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def surprise_spores(ctx):
    """Discarded from hand by the opponent's effect: discard their hand."""
    # "During your opponent's turn": an opposing effect that somehow discards
    # this from hand during the OWNER's turn does not trigger.
    if ctx.session.turn_state.active_player_id == ctx.player_id:
        return
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.discard_cards(hand)

card = PokemonCardDef(
    guid="7632dddb-eb5d-5bb1-bb77-38c2649203e4",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Ability(
            title="Surprise Spores",
            game_text="During your opponent's turn, if this Pokémon is discarded from your hand by an effect of an attack or Ability from your opponent's Pokémon, or by an effect of your opponent's Item or Supporter cards, discard your opponent's hand.",
            trigger=Triggers.ON_DISCARDED_FROM_HAND,
            effect=surprise_spores,
        ),
        Attack(
            title="Hypno Hammer",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
