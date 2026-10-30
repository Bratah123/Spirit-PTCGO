"""STUB: effect not implemented — do not guess mechanics.
Registeel ex (EX5 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import exoskeleton_passive, steel_wave

card = PokemonCardDef(
    guid="6cd617c6-bcc1-5725-96ac-39ac51d3c3f0",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeelex.Name",
    display_name="Registeel ex",
    searchable_by=["Registeel ex", "Basic", "ex", "Registeelex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=379,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Registeel ex by attacks is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=exoskeleton_passive(10),
        ),
        Attack(
            title="Steel Wave",
            game_text="Does 20 damage to each of your opponent's Benched Pok\u00e9mon of the same type as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=steel_wave(20),
        ),
    ],
)