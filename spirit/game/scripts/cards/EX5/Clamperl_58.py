"""STUB: effect not implemented — do not guess mechanics.
Clamperl (EX5 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.card_effects.ex import exoskeleton_passive

card = PokemonCardDef(
    guid="e17f412d-1111-5708-873d-3de2ccb7da17",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=366,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Clamperl by attacks is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=exoskeleton_passive(10),
        ),
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)