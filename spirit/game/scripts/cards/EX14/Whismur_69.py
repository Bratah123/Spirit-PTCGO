"""STUB: effect not implemented — do not guess mechanics.
Whismur (EX14 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="24c23464-a459-5218-92d4-1e74bd579850",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)