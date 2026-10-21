from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType, TrainerType
from spirit.game.content.definitions import def_for
from spirit.game.models.board import BoardState, TrainerEntity
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon, tool_slots_free
from spirit.game.session.effects import EffectContext


def _from_mega(calc, carrier):
    """Damage to the holder by an attack from the opponent's Mega Evolution Pokemon."""
    return (calc.target is carrier_pokemon(carrier) and calc.attacker is not None
            and "MEGA" in (getattr(def_for(calc.attacker.archetype_id), "subtypes", None) or []))


# The passive Klefki carries while attached as a Pokemon Tool.
WONDER_LOCK_TOOL = prevent_damage_when(_from_mega)

_AS_TOOL = {
    AttrID.CARD_TYPE: CardType.TRAINER.value,
    AttrID.TRAINER_TYPE: TrainerType.POKEMON_TOOL.value,
}


def _targets(board, player_id, me):
    return [p for p in board.pokemon_in_play(player_id)
            if p is not me and tool_slots_free(board, p) > 0]


def wonder_lock_condition(board, player_id, pokemon):
    parent = getattr(pokemon, "parent", None)
    return parent is not None and parent.get_attribute(AttrID.NAME) == "bench" \
        and bool(_targets(board, player_id, pokemon))


async def wonder_lock(ctx):
    """If this Pokemon is on your Bench, discard all cards attached to it and
    attach it to 1 of your Pokemon as a Pokemon Tool card (damage from the
    opponent's Mega Evolution Pokemon's attacks to the holder is prevented;
    discarded at the end of your opponent's turn)."""
    me = ctx.source
    targets = _targets(ctx.board, ctx.player_id, me)
    if not targets:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Pokémon to attach Klefki to as a Pokémon Tool")
    if target is None:
        return
    attached = list(me.children)
    if attached:
        await ctx.discard_cards(attached)
    session = ctx.session
    session.clear_pokemon_effects(me)
    session.reset_pokemon_damage(me)
    session.reset_ability_usage(me)
    BoardState.masquerade_as(me, TrainerEntity, _AS_TOOL, passive=WONDER_LOCK_TOOL)
    if not await ctx.attach_tool(me, target):
        BoardState.unmask(me)
        return
    eid = me.entity_id

    async def _discard_after_opponent_turn(sess):
        card = sess.board_state.get_entity(eid)
        if card is None or card.masquerade is None or card.parent is None:
            return
        dctx = EffectContext(sess, card.owning_player_id, card, None)
        await dctx.discard_cards([card])
        await sess._flush_effect_runs(dctx)

    ctx.schedule_at_checkup(1, _discard_after_opponent_turn)

card = PokemonCardDef(
    guid="3d9825f4-a971-5dab-b11a-740f1a72c34a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Ability(
            title="Wonder Lock",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may discard all cards attached to this Pok\u00e9mon and attach it to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. Prevent any damage done to the Pok\u00e9mon this card is attached to by attacks from your opponent's Mega Evolution Pok\u00e9mon. If this card is attached to a Pok\u00e9mon, discard this card at the end of your opponent's turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=wonder_lock_condition,
            effect=wonder_lock,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)