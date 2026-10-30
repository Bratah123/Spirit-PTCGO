"""STUB: effect not implemented — do not guess mechanics.
Rayquaza (EX9 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import bay_dance_boost


card = PokemonCardDef(
    guid="cb865e38-afdc-51fa-a3c3-c6bed04ed207",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Dance",
            game_text="During your next turn, if any of your current Active Pok\u00e9mon does damage to any Defending Pok\u00e9mon, the attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=bay_dance_boost(),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)