"""STUB: effect not implemented — do not guess mechanics.
Swalot (XY4 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="f8fc9a0b-9773-5194-a177-934a8f8e5fdb",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1", "Swalot"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Poison Gas",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Swallow Up",
            game_text="If, before doing damage, your opponent's Active Pok\u00e9mon has fewer remaining HP than this Pok\u00e9mon, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)