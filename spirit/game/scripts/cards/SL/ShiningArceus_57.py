"""STUB: effect not implemented — do not guess mechanics.
Shining Arceus (SL #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.sl import fabled_defense_passive


card = PokemonCardDef(
    guid="e6147f47-b51d-5d5c-ad9e-b21b5b445a3f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningArceus.Name",
    display_name="Shining Arceus",
    searchable_by=["Shining Arceus", "Basic", "ShiningArceus"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SL",
    rarity=Rarities.Shining,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Ability(
            title="Fabled Defense",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=fabled_defense_passive,
        ),
        Attack(
            title="Ultimate Arrow",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(30),
        ),
    ],
)