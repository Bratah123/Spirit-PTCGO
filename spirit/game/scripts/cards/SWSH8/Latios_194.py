from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _latias_in_play(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latias"
    ]


def blue_assist_condition(board, player_id, pokemon):
    if not _latias_in_play(board, player_id):
        return False
    hand_area = board.find_player_area(player_id, "hand")
    hand = hand_area.children if hand_area else []
    return any(
        is_energy_card(c) and energy_provides_type(c, PokemonTypes.PSYCHIC.value)
        for c in hand
    )


async def blue_assist(ctx):
    """Once per turn, you may attach a Psychic Energy card from your hand
    to 1 of your Latias."""
    latias_list = _latias_in_play(ctx.board, ctx.player_id)
    if not latias_list:
        return
    hand_energy = [
        c for c in ctx.hand()
        if is_energy_card(c) and energy_provides_type(c, PokemonTypes.PSYCHIC.value)
    ]
    if not hand_energy:
        return
    if not await ctx.ask_yes_no(
        "Attach a Psychic Energy card from your hand to 1 of your Latias?"
    ):
        return
    picks = await ctx.choose_cards(
        hand_energy, 1, prompt="Choose a Psychic Energy card to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(latias_list, "Choose 1 of your Latias")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="0797b843-dbbd-512b-9582-2f55389fb9cb",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Fusion Strike", "Latios"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=194,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=381,
    abilities=[
        Ability(
            title="Blue Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latias.",
            activation=Activations.ONCE_PER_TURN,
            condition=blue_assist_condition,
            effect=blue_assist,
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)