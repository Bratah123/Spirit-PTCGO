from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.trainers import opponent_has_bench


def _drive_off_condition(board, player_id, pokemon=None):
    return opponent_has_bench(board, player_id)


async def _drive_off(ctx):
    """Have your opponent switch their Active Pokemon with 1 of their Benched."""
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="e46b37c3-8309-518d-bf51-d2c9859b28dd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Ability(
            title="Drive Off",
            game_text="Once during your turn (before your attack), you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_drive_off_condition,
            effect=_drive_off,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)