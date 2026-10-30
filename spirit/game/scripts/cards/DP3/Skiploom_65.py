"""STUB: effect not implemented — do not guess mechanics.
Skiploom (DP3 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="81a57251-9148-5989-827d-cb50b9b91a91",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Skiploom"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Cotton Balloon",
            game_text="If Skiploom has any Grass Energy attached to it, any damage done to Skiploom by attacks from your opponent's Evolved Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="U-turn",
            game_text="Switch Skiploom with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)