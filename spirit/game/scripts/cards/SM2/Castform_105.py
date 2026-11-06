from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import AttrID, TrainerType
from spirit.game.card_effects.support_common import search_to_hand


from spirit.game.attributes import TrainerType


def _is_stadium_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


card = PokemonCardDef(
    guid="a11336c2-fea4-50d3-ab08-d9f002adbba0",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Attack(
            title="Weather Teller",
            game_text="Search your deck for up to 2 Stadium cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_stadium_card, count=2, minimum=0, prompt='Choose up to 2 Stadium cards'),
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)