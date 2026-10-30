"""STUB: effect not implemented — do not guess mechanics.
Spoink (EX9 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="daeda2bb-fa2e-56d5-9d7d-4d0e033febec",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    display_name="Spoink",
    searchable_by=["Spoink", "Basic", "Spoink"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=325,
    abilities=[
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)