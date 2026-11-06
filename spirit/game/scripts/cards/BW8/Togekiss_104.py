from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, TrainerType
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.passives_common import TrainerEffectShieldPassive
from spirit.game.models.board import PokemonEntity


class _BrightVeilPassive(TrainerEffectShieldPassive):
    """While this Pokemon is your Active, prevent all effects of your
    opponent's Item cards done to your Pokemon."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card, trainer_type, carrier,
                               affected_entity=None, board=None):
        if trainer_type != TrainerType.ITEM.value:
            return False
        return super().blocks_trainer_effects(affected_player_id, trainer_card, trainer_type,
                                              carrier, affected_entity, board)


card = PokemonCardDef(
    guid="3e41a8a1-1ef1-50f3-8e4a-23d4f056cd95",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Bright Veil",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever your opponent plays an Item card from his or her hand, prevent all effects of that card done to your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_BrightVeilPassive(supporters_only=False, protects=lambda e, c: isinstance(e, PokemonEntity), while_active=True),
        ),
        Attack(
            title="Return",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=draw_until_effect(6),
        ),
    ],
)