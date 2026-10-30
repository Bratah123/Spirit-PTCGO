"""STUB: effect not implemented — do not guess mechanics.
Omastar (DP5 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="c84dfd85-bbdc-5d64-8dab-f10f46631096",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Primal Swirl",
            game_text="Once during your turn, when you play Omastar from your hand to evolve 1 of your Pok\u00e9mon, you may remove the highest Stage Evolution card from each of your opponent's Benched Evolved Pok\u00e9mon and put those cards back into his or her hand. You can't use more than 1 Primal Swirl Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Send Back",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)