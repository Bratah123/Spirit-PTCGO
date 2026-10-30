"""STUB: effect not implemented — do not guess mechanics.
Holon's Voltorb (EX11 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="658be6b1-7434-54a7-9f5c-96883adf08bd",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsVoltorb.Name",
    display_name="Holon's Voltorb",
    searchable_by=["Holon's Voltorb", "Basic", "HolonsVoltorb"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)