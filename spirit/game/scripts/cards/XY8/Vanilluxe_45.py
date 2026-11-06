from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _supporter_or_stadium(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (TrainerType.SUPPORTER.value, TrainerType.STADIUM.value)


async def _frigid_breath(ctx):
    """30; until the end of your next turn, each player can't play Supporter or Stadium cards."""
    await ctx.deal_damage()
    through = ctx.session.turn_state.turn_number + 2
    ctx.lock_plays(ctx.player_id, _supporter_or_stadium, through)
    ctx.lock_plays(ctx.opponent_id, _supporter_or_stadium, through)


card = PokemonCardDef(
    guid="e54de397-71d5-56c7-9fd7-95ad6ad97d66",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Frigid Breath",
            game_text="Until the end of your next turn, each player can't play any Supporter or Stadium cards from his or her hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_frigid_breath,
        ),
        Attack(
            title="Deep Freeze",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed. If tails, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True,
                                    tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)