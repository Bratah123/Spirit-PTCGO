"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Claydol (EX4 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import clay_pulse
from spirit.game.card_effects.attacks_common import place_counters


card = PokemonCardDef(
    guid="e3404047-1365-58be-8cf6-eb0d5a666dfb",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasClaydol.Name",
    display_name="Team Magma's Claydol",
    searchable_by=["Team Magma's Claydol", "Stage 1", "TeamMagmasClaydol"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Clay Curse",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=place_counters(2, 'choose_any_opponent'),
        ),
        Attack(
            title="Clay Pulse",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=clay_pulse(),
        ),
    ],
)