"""STUB: effect not implemented — do not guess mechanics.
Giratina LV.X (DPP #DP38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a5cf91ab-5065-5640-9735-84b5ba48c56e",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaLVX.Name",
    display_name="Giratina LV.X",
    searchable_by=["Giratina LV.X", "Level-Up", "GiratinaLVX"],
    subtypes=["Level-Up"],
    collector_number=38,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    family_id=487,
    abilities=[
        Ability(
            title="Invisible Tentacles",
            game_text="Whenever your opponent's Pok\u00e9mon tries to attack, your opponent discards 1 card from his or her hand. (If your opponent can't discard 1 card, your opponent's Pok\u00e9mon can't attack.) You can't use more than 1 Invisible Tentacles Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Lost",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If any of your opponent's Pok\u00e9mon would be Knocked Out by damage from this attack, put that Pok\u00e9mon and all cards attached to it in the Lost Zone instead of discarding it.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)