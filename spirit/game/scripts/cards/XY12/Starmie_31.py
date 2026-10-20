from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


def _space_beacon_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    discard = board.find_player_area(player_id, "discard")
    return bool(hand and hand.children) and bool(discard and any(is_basic_energy_card(c) for c in discard.children))


async def _space_beacon(ctx):
    """Discard a card from your hand; if you do, put 2 basic Energy cards from
    your discard pile into your hand (not the one just discarded)."""
    gone = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card")
    if not gone:
        return
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c) and c not in gone]
    if pool:
        n = min(2, len(pool))
        picked = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 basic Energy cards")
        await ctx.put_in_hand(picked)


card = PokemonCardDef(
    guid="46ed468f-9eda-5f0e-b7aa-7ba9179bafe4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Space Beacon",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, put 2 basic Energy cards from your discard pile into your hand. (You can't choose a card you discarded with the effect of this Ability.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_space_beacon_condition,
            effect=_space_beacon,
        ),
        Attack(
            title="Star Freeze",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)