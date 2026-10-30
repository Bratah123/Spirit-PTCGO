from spirit.game.card_effects.ex import breaking_impact
"""STUB: effect not implemented — do not guess mechanics.
Dark Ariados (EX7 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="08bc6202-5342-55da-af82-7d78e7832138",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAriados.Name",
    display_name="Dark Ariados",
    searchable_by=["Dark Ariados", "Stage 1", "DarkAriados"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Super Poison Breath",
            game_text="Each Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Breaking Impact",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage for each Colorless Energy in that Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=breaking_impact(20),
        ),
    ],
)