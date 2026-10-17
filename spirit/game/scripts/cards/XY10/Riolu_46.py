"""STUB: effect not implemented — do not guess mechanics.
Riolu (XY10 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e51793bf-b308-5e5c-8a14-1a4497a422bd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic", "Riolu"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title="Smash Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)