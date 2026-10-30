"""STUB: effect not implemented — do not guess mechanics.
Cradily ex (EX4 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import primal_vibes_passive


card = PokemonCardDef(
    guid="5da3fb05-cd3a-5fa0-b4bb-598d9dd765de",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradilyex.Name",
    display_name="Cradily ex",
    searchable_by=["Cradily ex", "Stage 2", "ex", "Cradilyex"],
    subtypes=["Stage 2", "ex"],
    collector_number=90,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=346,
    abilities=[
        Ability(
            title="Primal Vibes",
            game_text="As long as Cradily ex is your Active Pok\u00e9mon, your opponent can't play a Pok\u00e9mon from his or her hand to evolve his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=primal_vibes_passive(),
        ),
        Attack(
            title="Eerie Light",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Acidic Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned and Burned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, SpecialConditions.BURNED),
        ),
    ],
)