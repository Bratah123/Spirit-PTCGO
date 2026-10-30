"""STUB: effect not implemented — do not guess mechanics.
Weepinbell (EX12 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="9da3f944-6610-55fd-ac83-206e0cd4b9a8",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1", "Weepinbell"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Sleep Seed",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)