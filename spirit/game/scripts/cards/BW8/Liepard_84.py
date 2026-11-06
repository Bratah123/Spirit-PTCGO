from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented, TRAINER_EFFECTS_BY_GUID
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_supporter_card


def _runnable_supporter(card):
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


async def _silent_claw(ctx):
    """Your opponent reveals their hand. Discard a Supporter card you find
    there and use its effect as the effect of this attack."""
    hand = await ctx.reveal_hand(ctx.opponent_id) or []
    supporters = [c for c in hand if is_supporter_card(c)]
    if not supporters:
        return
    picked = await ctx.choose_cards(supporters, 1, minimum=1,
                                    prompt="Choose a Supporter card to discard and use")
    if not picked:
        return
    card = picked[0]
    await ctx.discard_cards([card])
    if _runnable_supporter(card):
        await TRAINER_EFFECTS_BY_GUID[(card.archetype_id or "").lower()](ctx)


card = PokemonCardDef(
    guid="0a1e2799-7d34-5ae4-93ec-2bcaddaee058",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Team Plasma", "Liepard"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=84,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Silent Claw",
            game_text="Your opponent reveal his or her hand. Discard a Supporter card you find there. Use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_silent_claw,
        ),
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)