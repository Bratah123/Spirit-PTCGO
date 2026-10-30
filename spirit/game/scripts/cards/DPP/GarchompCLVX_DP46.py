"""STUB: effect not implemented — do not guess mechanics.
Garchomp C LV.X (DPP #DP46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="de23b221-dc44-5181-888d-f95dbfef1d36",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompCLVX.Name",
    display_name="Garchomp C LV.X",
    searchable_by=["Garchomp C LV.X", "Level-Up", "SP", "GarchompCLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=46,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    family_id=445,
    abilities=[
        Ability(
            title="Healing Breath",
            game_text="Once during your turn (before your attack), when you put Garchomp C LV.X from your hand onto your Active Garchomp C, you may remove all damage counters from each of your Pok\u00e9mon SP.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Rush",
            game_text="Discard 2 Energy attached to Garchomp C. Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Garchomp C can't use Dragon Rush during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)