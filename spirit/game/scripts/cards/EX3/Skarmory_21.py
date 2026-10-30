"""STUB: effect not implemented — do not guess mechanics.
Skarmory (EX3 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import pick_on_look, power_count

card = PokemonCardDef(
    guid="4289d850-7f06-5370-83a9-7716b5ca45ba",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=227,
    abilities=[
        Attack(
            title="Pick On",
            game_text="If the number of cards in your opponent's hand is at least 6, look at his or her hand. Choose a number of cards there until your opponent has 5 cards left in his or her hand and have your opponent shuffle the cards you chose into his or her deck.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=pick_on_look(5),
        ),
        Attack(
            title="Power Count",
            game_text="Count the amount of Energy attached to all of your Pok\u00e9mon and all of your opponent's Pok\u00e9mon. If your Pok\u00e9mon have less Energy than your opponent's, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=power_count(20, 30),
        ),
    ],
)