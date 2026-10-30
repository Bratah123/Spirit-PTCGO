"""STUB: effect not implemented — do not guess mechanics.
Aron (EX16 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dig_deep_energy_to_hand


card = PokemonCardDef(
    guid="daa9542b-f60c-5a17-ae63-73c37303c21a",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic", "Aron"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=304,
    abilities=[
        Attack(
            title="Dig Deep",
            game_text="Search your discard pile for an Energy card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dig_deep_energy_to_hand(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)