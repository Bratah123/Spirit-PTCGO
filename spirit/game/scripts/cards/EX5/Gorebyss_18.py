"""STUB: effect not implemented — do not guess mechanics.
Gorebyss (EX5 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import mystic_water


card = PokemonCardDef(
    guid="bbf89e8f-e5dc-54d9-ab26-c07f7aed56dc",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1", "Gorebyss"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Stun Needle",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Mystic Water",
            game_text="Does 20 damage plus 10 more damage for each Psychic Energy in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=mystic_water(),
        ),
    ],
)