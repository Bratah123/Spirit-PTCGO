"""STUB: effect not implemented — do not guess mechanics.
Ledyba δ (EX15 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="07cb1fc9-fc81-5669-9395-0408bf7d29dc",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    display_name="Ledyba δ",
    searchable_by=["Ledyba \u03b4", "Basic", "Ledyba"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=165,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)