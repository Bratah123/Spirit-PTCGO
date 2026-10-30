"""STUB: effect not implemented — do not guess mechanics.
Palkia LV.X (DPP #DP18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0bcc4048-407f-57a3-a7b5-9723984fad22",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaLVX.Name",
    display_name="Palkia LV.X",
    searchable_by=["Palkia LV.X", "Level-Up", "PalkiaLVX"],
    subtypes=["Level-Up"],
    collector_number=18,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.LEVELUP,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    family_id=484,
    abilities=[
        Ability(
            title="Restructure",
            game_text="Once during your turn (before your attack), you may have your opponent switch 1 of your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. Then, you switch 1 of the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. This power can't be used if Palkia is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Reflect",
            game_text="You may move all Energy cards attached to Palkia to your Benched Pok\u00e9mon in any way you like. (Ignore this effect if you don't have any Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)