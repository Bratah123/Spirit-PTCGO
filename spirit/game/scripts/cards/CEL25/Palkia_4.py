from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot, boost_own_next_turn


class AbsoluteSpacePassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


card = PokemonCardDef(
    guid="70959369-220f-5338-bdef-cfebe8044717",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Ability(
            title="Absolute Space",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Stadium cards from their hand.",
            passive=AbsoluteSpacePassive(),
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=boost_own_next_turn(80, attack_title="Overdrive Smash"),
        ),
    ],
)