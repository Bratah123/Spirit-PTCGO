from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID, TrainerType
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.support_common import search_to_hand


def _is_stadium_card(card):
    return (
        is_trainer_card(card)
        and card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
    )


card = PokemonCardDef(
    guid="89d00e69-d879-575c-a0fa-a25bb2fe797b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Nest Building",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_stadium_card, count=1, minimum=0, reveal=True, prompt='Choose a Stadium card to put into your hand.'),
        ),
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)