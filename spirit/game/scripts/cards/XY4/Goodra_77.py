from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.session.passives import Passive


class _SlipTrip(Passive):
    """Neither player can attach Pokemon Tool cards from hand."""
    def blocks_trainer_play(self, card, player_id, carrier):
        return card.get_attribute(AttrID.TRAINER_TYPE) in (
            TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


card = PokemonCardDef(
    guid="f73a0604-adc7-51b1-818f-200e00ed085f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Slip Trip",
            game_text="Each player can't attach any Pok\u00e9mon Tool cards from his or her hand to any of his or her Pok\u00e9mon.",
            passive=_SlipTrip(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=mill_attack(1, opponent=False),
        ),
    ],
)