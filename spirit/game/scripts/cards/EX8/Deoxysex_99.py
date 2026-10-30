"""STUB: effect not implemented — do not guess mechanics.
Deoxys ex (EX8 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys, psychic_shield_ex


card = PokemonCardDef(
    guid="c39e614e-9bd4-50dd-b4b0-097f7c74199b",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxysex.Name",
    display_name="Deoxys ex",
    searchable_by=["Deoxys ex", "Basic", "ex", "Deoxysex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys ex and switch it with Deoxys ex. (Any cards attached to Deoxys ex, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys ex on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            shared_once_per_turn="Form Change",
            # STUB: ability effect not implemented
            effect=form_change_deoxys(ex=True),
        ),
        Attack(
            title="Psychic Shield",
            game_text="Prevent all effects of attacks, including damage, done to Deoxys ex by your opponent's Pok\u00e9mon-ex during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=psychic_shield_ex(),
        ),
    ],
)