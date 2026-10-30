"""STUB: effect not implemented — do not guess mechanics.
Sunkern (EX10 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import minor_errand_running


card = PokemonCardDef(
    guid="83c51430-03f1-57ce-9955-cb32cf8926ed",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic", "Sunkern"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=191,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=minor_errand_running(1),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)