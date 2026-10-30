"""STUB: effect not implemented — do not guess mechanics.
Illumise (EX11 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import beacon_protection_passive, call_for_family_basic, confuse_if_evolved


card = PokemonCardDef(
    guid="a61c120c-8373-50b5-9691-7a8ad9a5fe48",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Ability(
            title="Beacon Protection",
            game_text="As long as you have Volbeat in play, prevent all effects, including damage, done to Illumise by attacks from your opponent's Pok\u00e9mon that has Dark in its name.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=beacon_protection_passive('Volbeat'),
            effect=None,
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_basic(),
        ),
        Attack(
            title="Strange Rasping",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=confuse_if_evolved(),
        ),
    ],
)