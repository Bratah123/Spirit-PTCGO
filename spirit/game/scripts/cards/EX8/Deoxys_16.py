"""STUB: effect not implemented — do not guess mechanics.
Deoxys (EX8 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys, link_blast


card = PokemonCardDef(
    guid="be661a45-e2c7-511c-81f0-56ce58ccf82f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            shared_once_per_turn="Form Change",
            # STUB: ability effect not implemented
            effect=form_change_deoxys(),
        ),
        Attack(
            title="Link Blast",
            game_text="If Deoxys and the Defending Pok\u00e9mon have a different amount of Energy attached to them, this attack's base damage is 20 instead of 40.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=link_blast(40, 20),
        ),
    ],
)