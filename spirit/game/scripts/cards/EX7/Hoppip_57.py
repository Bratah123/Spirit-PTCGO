"""STUB: effect not implemented — do not guess mechanics.
Hoppip (EX7 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import miracle_powder, buffer_passive


card = PokemonCardDef(
    passive=buffer_passive(),
    guid="de5340e2-0cb6-5bae-b935-6582cc80cfcd",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    display_name="Hoppip",
    searchable_by=["Hoppip", "Basic", "Hoppip"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=187,
    abilities=[
        Ability(
            title="Buffer",
            game_text="If Hoppip would be Knocked Out by an opponent's attack, flip a coin. If heads, Hoppip is not Knocked Out and its remaining HP becomes 10 instead.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose 1 Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=miracle_powder(),
        ),
    ],
)