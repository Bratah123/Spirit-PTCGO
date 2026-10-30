"""STUB: effect not implemented — do not guess mechanics.
Castform Snow-Cloud Form (DP6 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_all_opponents


card = PokemonCardDef(
    guid="34123a6b-a4e5-5546-9912-900e8670a5ef",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSnowCloudForm.Name",
    display_name="Castform Snow-Cloud Form",
    searchable_by=["Castform Snow-Cloud Form", "Basic", "CastformSnowCloudForm"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=351,
    abilities=[
        Ability(
            title="Temperament",
            game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Snow-cloud Form. (Any cards attached to Castform Snow-cloud Form, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform Snow-cloud Form back into your deck. You can't use more than 1 Temperament Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hail",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(10),
        ),
    ],
)