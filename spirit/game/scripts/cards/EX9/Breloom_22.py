"""STUB: effect not implemented — do not guess mechanics.
Breloom (EX9 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.card_effects.ex import extra_energy_damage
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="a95f7e69-1fc8-50b9-91c8-5a69ff18d230",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Power Blow",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Breloom.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_energy_damage(10, base=10),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)