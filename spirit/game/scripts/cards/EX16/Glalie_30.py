"""STUB: effect not implemented — do not guess mechanics.
Glalie (EX16 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import glalie_synergy_reduce
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


card = PokemonCardDef(
    guid="e982e4e0-4230-5a88-8a90-2b68dd27b5e4",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Synergy Effect",
            game_text="If Glacia's Stadium is in play, any damage done to Glalie by attacks from your opponent's Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=glalie_synergy_reduce(30),
        ),
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Double-edge",
            game_text="Glalie does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=recoil_attack(10),
        ),
    ],
)