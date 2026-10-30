"""STUB: effect not implemented — do not guess mechanics.
Sableye (EX16 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import down_draw, feint_attack, sableye_synergy_prevent


card = PokemonCardDef(
    guid="cb1da73a-a9c1-5515-8718-44ba66e854fb",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=302,
    abilities=[
        Ability(
            title="Synergy Effect",
            game_text="If Phoebe's Stadium is in play, prevent all damage done to Sableye by attacks from your opponent's Pok\u00e9mon-ex.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=sableye_synergy_prevent(),
        ),
        Attack(
            title="Down Draw",
            game_text="Draw 2 cards from the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=down_draw(2),
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=feint_attack(20),
        ),
    ],
)