from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_energy_card


def _is_water_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


def _double_gunner_condition(board, player_id, pokemon):
    opponent_id = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(opponent_id, "bench") if opponent_id else None
    if not bench or not bench.children:
        return False
    return requires_hand(_is_water_energy)(board, player_id, pokemon)


async def _double_gunner(ctx):
    """Discard a Water Energy from hand; choose 2 of the opponent's Benched
    Pokemon and put 2 damage counters on each."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_water_energy,
        prompt="Discard a Water Energy card to use Double Gunner",
    )
    if not discarded:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    targets = await ctx.choose_cards(
        bench, 2, minimum=1, prompt="Choose up to 2 of your opponent's Benched Pokémon",
    )
    for target in targets:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


async def _g_max_spiral(ctx):
    """70, +70 more if you put an attached Energy into your hand."""
    energies = ctx.attached_energies(ctx.attacker)
    bonus = 0
    if energies and await ctx.ask_yes_no(
        "Put an Energy attached to this Pokémon into your hand? If you do, this attack does 70 more damage."
    ):
        picks = await ctx.choose_cards(
            energies, 1, prompt="Choose an Energy card to put into your hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
            bonus = 70
    await ctx.deal_damage(70 + bonus)


card = PokemonCardDef(
    guid="ce99ea43-7ce3-57c6-9c1f-c7cb7e38938a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonVMAX.Name",
    display_name="Inteleon VMAX",
    searchable_by=["Inteleon VMAX", "VMAX", "Rapid Strike", "InteleonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=79,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    family_id=818,
    abilities=[
        Ability(
            title="Double Gunner",
            game_text="You must discard a Water Energy card from your hand in order to use this Ability. Once during your turn, you may choose 2 of your opponent's Benched Pokémon and put 2 damage counters on each of them.",
            activation=Activations.ONCE_PER_TURN,
            condition=_double_gunner_condition,
            effect=_double_gunner,
        ),
        Attack(
            title="G-Max Spiral",
            game_text="You may put an Energy attached to this Pokémon into your hand. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=_g_max_spiral,
        ),
    ],
)
