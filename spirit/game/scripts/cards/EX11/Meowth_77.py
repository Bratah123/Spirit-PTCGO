"""STUB: effect not implemented — do not guess mechanics.
Meowth (EX11 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dig_deep_energy_to_hand


card = PokemonCardDef(
    guid="2998fd63-5785-5527-9eb5-594f43a07520",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Pickup Power",
            game_text="Search your discard pile for an Energy card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dig_deep_energy_to_hand(),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)