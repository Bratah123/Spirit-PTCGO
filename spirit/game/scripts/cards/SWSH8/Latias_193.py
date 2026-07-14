from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_vmax


def _psychic_energy_in_hand(ctx):
    return [
        c for c in ctx.hand()
        if is_basic_energy_card(c)
        and PokemonTypes.PSYCHIC.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
    ]


def _my_latios(ctx):
    return [
        p for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latios"
    ]


def _red_assist_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(
        is_basic_energy_card(c)
        and PokemonTypes.PSYCHIC.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
        for c in hand.children
    ):
        return False
    return any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latios"
        for p in board.pokemon_in_play(player_id)
    )


async def _red_assist(ctx):
    energies = _psychic_energy_in_hand(ctx)
    targets = _my_latios(ctx)
    if not energies or not targets:
        return
    if not await ctx.ask_yes_no(
        "Attach a Psychic Energy card from your hand to 1 of your Latios?"
    ):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Psychic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(targets, "Choose the Latios to attach it to")
    if target is not None:
        await ctx.attach_energy(picked[0], target)


async def _dyna_barrier(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker,
        prevent_damage_when(
            lambda calc, carrier: calc.attacker is not None
            and is_pokemon_vmax(calc.attacker.archetype_id)
        ),
    )


card = PokemonCardDef(
    guid="50c1332e-cf73-5e50-9daf-c50ca23daa51",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Fusion Strike", "Latias"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=193,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Ability(
            title="Red Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latios.",
            activation=Activations.ONCE_PER_TURN,
            condition=_red_assist_condition,
            effect=_red_assist,
        ),
        Attack(
            title="Dyna Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_dyna_barrier,
        ),
    ],
)