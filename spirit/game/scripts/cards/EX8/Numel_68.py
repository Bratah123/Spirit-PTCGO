"""STUB: effect not implemented — do not guess mechanics.
Numel (EX8 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dense_vs_evolved


card = PokemonCardDef(
    guid="b3daf1b4-5d4b-5b8a-96b9-22161a4e184f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic", "Numel"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Ability(
            title="Dense",
            game_text="Any damage done to Numel by attacks from Evolved Pok\u00e9mon (both yours and your opponent's) is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=dense_vs_evolved(),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)