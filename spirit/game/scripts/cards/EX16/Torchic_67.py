"""STUB: effect not implemented — do not guess mechanics.
Torchic (EX16 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="2bb5bae7-9ed1-5131-b4e8-ae8c98a39619",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Super Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)