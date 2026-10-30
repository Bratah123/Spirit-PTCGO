"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Cacnea (EX4 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import pin_missile


card = PokemonCardDef(
    guid="0d21d054-91cb-5a65-9e93-973ec8f086e6",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCacnea.Name",
    display_name="Team Aqua's Cacnea",
    searchable_by=["Team Aqua's Cacnea", "Basic", "TeamAquasCacnea"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=331,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=pin_missile(4, 10),
        ),
    ],
)