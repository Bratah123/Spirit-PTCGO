from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.effects import full_stack


async def _cacophony(ctx):
    """At the end of your opponent's next turn, discard the Defending Pokemon and all cards attached to it."""
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    target_id = d.entity_id

    async def _discard(session):
        target = session.board_state.get_entity(target_id)
        parent = getattr(target, "parent", None)
        if target is None or parent is None or parent.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
            return
        from spirit.game.session.effects import EffectContext
        c = EffectContext(session, ctx.player_id, ctx.source, ctx.ability)
        await c.discard_cards(full_stack(target))
        await c.flush_choreography()
        await session.enforce_bench_capacity()

    ctx.schedule_at_checkup(1, _discard)


card = PokemonCardDef(
    guid="92bb50ab-605d-5c2c-a3c4-5c63908f059f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
        Attack(
            title="Cacophony",
            game_text="At the end of your opponent's next turn, discard the Defending Pok\u00e9mon and all cards attached to it.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_cacophony,
        ),
    ],
)