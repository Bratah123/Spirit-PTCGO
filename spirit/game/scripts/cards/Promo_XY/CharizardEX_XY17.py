from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.content.definitions import def_for


def _is_m(card):
    return getattr(def_for(card.archetype_id), "display_name", None) == "M Charizard-EX"


card = PokemonCardDef(
    guid="bd4f7dd0-0771-5a60-86c3-50d87dcf964a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    display_name="Charizard-EX",
    searchable_by=["Charizard-EX", "Basic", "EX", "CharizardEX"],
    subtypes=["Basic", "EX"],
    collector_number=17,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Mega Ascension",
            game_text="Search your deck for M Charizard-EX, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_m, count=1, minimum=0, reveal=True, prompt="Choose M Charizard-EX"),
        ),
        Attack(
            title="Brave Fire",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)