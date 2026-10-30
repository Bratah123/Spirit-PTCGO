"""STUB: effect not implemented — do not guess mechanics.
Bagon δ (EX11 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import discard_energy_typed
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c2f7d41-32e5-5755-8d82-b8e922f966b8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon δ",
    searchable_by=["Bagon \u03b4", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    family_id=371,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard a Fire Energy card attached to Bagon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=discard_energy_typed(PokemonTypes.FIRE),
        ),
    ],
)