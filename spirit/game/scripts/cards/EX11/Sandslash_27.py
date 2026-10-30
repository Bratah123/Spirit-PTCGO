"""STUB: effect not implemented — do not guess mechanics.
Sandslash δ (EX11 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.card_effects.ex import delta_storm_between_turns, rend
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="21a18ccb-fb75-5d09-9fbe-135d86bb15f6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash δ",
    searchable_by=["Sandslash \u03b4", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Delta Storm",
            game_text="As long as Sandslash is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon-ex between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=delta_storm_between_turns(1),
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=rend(20, 20),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)