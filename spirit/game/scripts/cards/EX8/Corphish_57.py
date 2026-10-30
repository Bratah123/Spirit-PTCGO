"""STUB: effect not implemented — do not guess mechanics.
Corphish (EX8 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="f34e8e28-091f-567d-9860-0fba40948ebb",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic", "Corphish"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Corphish by attacks is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=takes_less_passive(10),
        ),
        Attack(
            title="Double Chop",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)