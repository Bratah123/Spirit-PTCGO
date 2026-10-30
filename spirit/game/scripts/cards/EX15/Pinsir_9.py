"""STUB: effect not implemented — do not guess mechanics.
Pinsir δ (EX15 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_call_search, pinsir_armor_vs_hand5
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8f037289-0e10-5ced-8b61-4cfc77e89658",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir δ",
    searchable_by=["Pinsir \u03b4", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Ability(
            title="Armor",
            game_text="If your opponent has 5 of more cards in his or her hand, any damage done to Pinsir by attacks is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=pinsir_armor_vs_hand5(30),
        ),
        Attack(
            title="Delta Call",
            game_text="Search your deck for a Pok\u00e9mon that has \u03b4 on its card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=delta_call_search(),
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)