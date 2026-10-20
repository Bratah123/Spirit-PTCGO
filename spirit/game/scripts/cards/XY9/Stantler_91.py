"""STUB: effect not implemented — do not guess mechanics.
Stantler (XY9 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="81aed745-5abf-53ce-9990-91916866b733",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Mystifying Horns",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Big Charge",
            game_text="If you have any Mega Evolution Pok\u00e9mon on your Bench, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)