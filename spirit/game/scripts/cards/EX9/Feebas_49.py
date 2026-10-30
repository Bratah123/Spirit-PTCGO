"""STUB: effect not implemented — do not guess mechanics.
Feebas (EX9 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import submerge_all_attacks_passive


card = PokemonCardDef(
    guid="5b2174dd-f0f9-575b-9d85-390663fbafad",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as Feebas is on your Bench, prevent all damage done to Feebas by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=submerge_all_attacks_passive(),
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)