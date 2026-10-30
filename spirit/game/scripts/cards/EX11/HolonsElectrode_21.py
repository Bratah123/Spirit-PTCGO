"""STUB: effect not implemented — do not guess mechanics.
Holon's Electrode (EX11 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="074fb7f2-a83a-5baf-a968-8fb8c97af777",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsElectrode.Name",
    display_name="Holon's Electrode",
    searchable_by=["Holon's Electrode", "Stage 1", "HolonsElectrode"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsVoltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)