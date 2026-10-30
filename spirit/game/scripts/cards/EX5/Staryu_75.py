"""STUB: effect not implemented — do not guess mechanics.
Staryu (EX5 #75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import core_guard_passive

card = PokemonCardDef(
    guid="7b2612fe-f55b-5803-9f5a-cc137d956528",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Staryu"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Ability(
            title="Core Guard",
            game_text="If Staryu has any Psychic Energy attached to it, damage done to Staryu by any attack is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=core_guard_passive(10),
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)