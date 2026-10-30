"""STUB: effect not implemented — do not guess mechanics.
Pikachu δ (EX12 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="fcbd9f90-ff69-557d-940f-75aaf9dbbd3b",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu δ",
    searchable_by=["Pikachu \u03b4", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="EX12",
    rarity=Rarities.RareSecret,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)