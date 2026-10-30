"""STUB: effect not implemented — do not guess mechanics.
Tyrogue (EX10 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution_any, baby_evolution_any_condition

card = PokemonCardDef(
    guid="79e2ea2c-54d2-5b58-b060-f35beceaf117",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Basic", "Tyrogue"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Ability(
            title="Baby Evolution",
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_any_condition("Hitmonlee", "Hitmonchan", "Hitmontop"),
            game_text="Once during your turn (before your attack), you may put Hitmonlee, Hitmonchan, or Hitmontop from your hand onto Tyrogue (this counts as evolving Tyrogue) and remove all damage counters from Tyrogue.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=baby_evolution_any("Hitmonlee", "Hitmonchan", "Hitmontop"),
        ),
        Attack(
            title="Desperate Punch",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play your opponent has more than you.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=baby_evolution_any("Hitmonlee", "Hitmonchan", "Hitmontop"),
        ),
    ],
)