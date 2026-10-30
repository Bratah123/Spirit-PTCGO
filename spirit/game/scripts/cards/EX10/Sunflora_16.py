"""STUB: effect not implemented — do not guess mechanics.
Sunflora (EX10 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.ex import dazzle_dance_confuse
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="5ec76c7e-7210-5868-b8b2-050547734d56",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Dazzle Dance",
            game_text="Each Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=dazzle_dance_confuse(),
        ),
        Attack(
            title="Green Blast",
            game_text="Does 20 damage plus 10 more damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)