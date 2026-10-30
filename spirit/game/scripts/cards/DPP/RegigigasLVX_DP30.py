"""STUB: effect not implemented — do not guess mechanics.
Regigigas LV.X (DPP #DP30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e76a4c3a-5733-5cd2-87b7-05588204a763",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasLVX.Name",
    display_name="Regigigas LV.X",
    searchable_by=["Regigigas LV.X", "Level-Up", "RegigigasLVX"],
    subtypes=["Level-Up"],
    collector_number=30,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    family_id=486,
    abilities=[
        Ability(
            title="Sacrifice",
            game_text="Once during your turn (before your attack), you may choose 1 of your Pok\u00e9mon in play and that Pok\u00e9mon is Knocked Out. Then, search your discard pile for up to 2 basic Energy cards, attach them to Regigigas, and remove 8 damage counters from Regigigas. This power can't be used if Regigigas is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giga Blaster",
            game_text="Discard the top card from your opponent's deck. Then, choose 1 card from your opponent's hand without looking and discard it. Regigigas can't use Giga Blaster during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)