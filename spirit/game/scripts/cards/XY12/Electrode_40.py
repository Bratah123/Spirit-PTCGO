from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from spirit.game.models.board import BoardState, EnergyEntity
from spirit.game.session.passives import effective_pokemon_types
from spirit.game.session.effects import EffectContext

_L = PokemonTypes.LIGHTNING.value
# Attached as a Special Energy: provides 2 Lightning Energy.
_AS_ENERGY = {
    AttrID.CARD_TYPE: CardType.ENERGY.value,
    AttrID.IS_SPECIAL_ENERGY: True,
    AttrID.ENERGY_INFO: {"options": [[_L, _L]]},
}


def _targets(board, player_id, me):
    return [p for p in board.pokemon_in_play(player_id)
            if p is not me and _L in effective_pokemon_types(board, p)]


def buzzap_condition(board, player_id, pokemon):
    return bool(_targets(board, player_id, pokemon))


async def buzzap_thunder(ctx):
    """Knock Out this Pokemon and attach it to one of your Lightning Pokemon
    as a Special Energy card that provides 2 Lightning Energy."""
    me = ctx.source
    targets = _targets(ctx.board, ctx.player_id, me)
    if not targets:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Lightning Pokémon to attach Electrode to as Energy")
    if target is None or not await ctx.knock_out(me):
        return
    session, pid, eid, tid = ctx.session, ctx.player_id, me.entity_id, target.entity_id

    async def _attach_as_energy():
        board = session.board_state
        card, holder = board.get_entity(eid), board.get_entity(tid)
        if card is None or holder is None or card.parent is None \
                or card.parent.get_attribute(AttrID.NAME) != "discard" \
                or holder not in board.pokemon_in_play(pid):
            return
        BoardState.masquerade_as(card, EnergyEntity, _AS_ENERGY)
        actx = EffectContext(session, pid, card, None)
        if not await actx.attach_energy(card, holder):
            BoardState.unmask(card)
            return
        await session._flush_effect_runs(actx)

    # After the Knock Out resolves (prize taken, stack discarded).
    ctx.deferred_actions.append(_attach_as_energy)

card = PokemonCardDef(
    guid="91e58ac5-0fc5-577c-b615-a0d20092a684",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Buzzap Thunder",
            game_text="Once during your turn (before your attack), you may Knock Out this Pok\u00e9mon and attach it to one of your Lightning Pok\u00e9mon as a Special Energy card. This card provides 2 Lightning Energy only while this card is attached to a Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=buzzap_condition,
            effect=buzzap_thunder,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)