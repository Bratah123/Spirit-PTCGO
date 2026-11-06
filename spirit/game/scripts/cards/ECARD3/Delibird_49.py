from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import is_tm_or_tool
from spirit.game.card_effects.support_common import gust_attack, search_to_hand


card = PokemonCardDef(
    guid="97445aa1-48cf-50a6-904c-b9e715735cb7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Limited Delivery",
            game_text="Search your deck for a Technical Machine or Pok\u00e9mon Tool card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                is_tm_or_tool, count=1, minimum=0, reveal=True,
                prompt="Choose a Technical Machine or Pokémon Tool card.",
            ),
        ),
        Attack(
            title="Kick Away",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)
