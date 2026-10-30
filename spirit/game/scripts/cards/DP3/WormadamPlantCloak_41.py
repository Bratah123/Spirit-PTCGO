"""STUB: effect not implemented — do not guess mechanics.
Wormadam Plant Cloak (DP3 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="39645db9-f55d-57e9-be2b-e41f1a94cc86",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamPlantCloak.Name",
    display_name="Wormadam Plant Cloak",
    searchable_by=["Wormadam Plant Cloak", "Stage 1", "WormadamPlantCloak"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Plant Cloak",
            game_text="If Wormadam Plant Cloak has 2 or more Grass Energy attached to it, Wormadam Plant Cloak gets +40 HP.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Hurricane",
            game_text="If the Defending Pok\u00e9mon has fewer remaining HP than Wormadam Plant Cloak, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)