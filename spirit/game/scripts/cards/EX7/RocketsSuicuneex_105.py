from spirit.game.card_effects.ex import hyper_splash, dark_and_clear_passive
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Suicune ex (EX7 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    passive=dark_and_clear_passive(),
    guid="b495c916-a939-5958-99e0-25961e089470",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSuicuneex.Name",
    display_name="Rocket's Suicune ex",
    searchable_by=["Rocket's Suicune ex", "Basic", "ex", "RocketsSuicuneex"],
    subtypes=["Basic", "ex"],
    collector_number=105,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Dark and Clear",
            game_text="As long as Rocket's Suicune ex has any Darkness Energy attached to it, Rocket's Suicune ex can't be affected by any Special Conditions.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Icy Wind",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Hyper Splash",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, this attack does 50 damage plus 40 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hyper_splash(),
        ),
    ],
)