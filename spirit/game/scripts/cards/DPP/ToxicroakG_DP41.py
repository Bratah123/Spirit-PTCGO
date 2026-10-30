"""STUB: effect not implemented — do not guess mechanics.
Toxicroak G (DPP #DP41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="22c6a323-a47e-5a42-a99b-cd4c68b8b5d9",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxicroakG.Name",
    display_name="Toxicroak G",
    searchable_by=["Toxicroak G", "Basic", "SP", "ToxicroakG"],
    subtypes=["Basic", "SP"],
    collector_number=41,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=454,
    abilities=[
        Ability(
            title="Leap Away",
            game_text="Once during your turn (before your attack), if Toxicroak G is your Active Pok\u00e9mon, you may flip a coin. If heads, return Toxicroak G and all cards attached to it to your hand. This power can't be used if Toxicroak G is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, this attack does 20 damage plus 40 more damage and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)