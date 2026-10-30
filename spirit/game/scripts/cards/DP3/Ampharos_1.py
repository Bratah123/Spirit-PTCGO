"""STUB: effect not implemented — do not guess mechanics.
Ampharos (DP3 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="256da3ec-839d-566d-b6ad-bbd822345b22",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Jamming",
            game_text="After your opponent plays a Supporter card from his or her hand, put 1 damage counter on each of your opponent's Pok\u00e9mon. You can't use more than 1 Jamming Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cluster Bolt",
            game_text="You may discard all Lightning Energy attached to Ampharos. If you do, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)