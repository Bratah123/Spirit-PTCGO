from spirit.game.data_utils import PokemonCardDef, Attack, Ability, TRAINER_EFFECTS_BY_GUID, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card


def _runnable_supporter(card):
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


def _primate_acting_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    discard = board.find_player_area(opponent_id, "discard")
    return bool(discard) and any(_runnable_supporter(c) for c in discard.children)


async def primate_acting(ctx):
    """Choose a Supporter card from the opponent's discard pile and use its
    effect as the effect of this attack."""
    candidates = [c for c in ctx.discard_pile(ctx.opponent_id) if _runnable_supporter(c)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Supporter card from your opponent's discard pile",
    )
    if not picked:
        return
    effect = TRAINER_EFFECTS_BY_GUID[(picked[0].archetype_id or "").lower()]
    await effect(ctx)


card = PokemonCardDef(
    guid="eafa4d0e-eb5e-5eea-a370-7b74de785952",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Attack(
            title="Primate Acting",
            game_text="Choose a Supporter card from your opponent's discard pile and use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_primate_acting_condition,
            effect=primate_acting,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)