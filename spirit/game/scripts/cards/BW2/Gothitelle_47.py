from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, AbilityTypes, TrainerType,
)
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class MagicRoomPassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM.value


card = PokemonCardDef(
    guid="538afe62-a391-5f27-8feb-75445511f0f4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Magic Room",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent can't play any Item cards from his or her hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=MagicRoomPassive(),
        ),
        Attack(
            title="Madkinesis",
            game_text="Does 20 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.PSYCHIC),
                20, base=30,
            ),
        ),
    ],
)
