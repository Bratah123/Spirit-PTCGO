"""STUB: effect not implemented — do not guess mechanics.
Mawile (EX16 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_basic, pull_away_to_4


card = PokemonCardDef(
    guid="60fbb983-42da-5071-b2a7-b1ee68f8252b",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=303,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_basic(),
        ),
        Attack(
            title="Pull Away",
            game_text="If your opponent has 5 or more cards in his or her hand, your opponent discards a number of cards until your opponent has 4 cards left in his or her hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=pull_away_to_4(),
        ),
    ],
)