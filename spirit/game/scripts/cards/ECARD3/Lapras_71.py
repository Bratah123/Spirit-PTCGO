from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="d7e7c245-caa5-55de-8152-67d2e1e8d8f1",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Assist",
            game_text="Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(
                is_supporter_card, count=1, reveal=True,
                prompt="Choose a Supporter card.",
            ),
        ),
        Attack(
            title="Hypnoblast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)
