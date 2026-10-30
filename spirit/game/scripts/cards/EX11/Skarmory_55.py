"""STUB: effect not implemented — do not guess mechanics.
Skarmory (EX11 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import cry_for_help, shining_horn_solo_passive, steel_wing_reduce
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4762f0f5-be9b-552b-9269-f614a8de1691",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=227,
    abilities=[
        Ability(
            title="Shining Horn",
            game_text="As long as Skarmory is the only Pok\u00e9mon you have in play, your opponent's Basic Pok\u00e9mon can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=shining_horn_solo_passive(),
            effect=None,
        ),
        Attack(
            title="Cry for Help",
            game_text="Search your deck for a Metal Pok\u00e9mon (excluding Pok\u00e9mon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cry_for_help(PokemonTypes.METAL),
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to Skarmory by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=steel_wing_reduce(20),
        ),
    ],
)