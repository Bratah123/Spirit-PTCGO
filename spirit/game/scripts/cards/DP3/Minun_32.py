"""STUB: effect not implemented — do not guess mechanics.
Minun (DP3 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8390795d-0fbf-524c-87b4-a85d48ace423",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=312,
    abilities=[
        Ability(
            title="Minus Charge",
            game_text="Once during your turn (before your attack), if any Pok\u00e9mon were Knocked Out during your opponent's last turn, you may draw 2 cards. You can't use more than 1 Minus Charge Pok\u00e9-Power each turn. This power can't be used if Minun is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tag Play \u2014",
            game_text="If you have Plusle on your Bench, you may move an Energy card attached to Minun to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)