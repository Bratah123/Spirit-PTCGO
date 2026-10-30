"""STUB: effect not implemented — do not guess mechanics.
Cresselia LV.X (DP4 #103): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9edbc309-7b06-5109-968d-56e513c8d8a2",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CresseliaLVX.Name",
    display_name="Cresselia LV.X",
    searchable_by=["Cresselia LV.X", "Level-Up", "CresseliaLVX"],
    subtypes=["Level-Up"],
    collector_number=103,
    set_code="DP4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    family_id=488,
    abilities=[
        Ability(
            title="Full Moon Dance",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from either player's Pok\u00e9mon to another Pok\u00e9mon (yours or your opponent's). This power can't be used if Cresselia is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moon Skip",
            game_text="If the Defending Pok\u00e9mon is Knocked Out by this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)