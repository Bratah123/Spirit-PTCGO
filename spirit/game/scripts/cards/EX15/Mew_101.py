"""STUB: effect not implemented — do not guess mechanics.
Mew ★ δ (EX15 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import mimicry_copy_any_opp_attack, rainbow_wave_per_type
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3bb549a-52e9-56fe-91df-8617e27b1288",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew ★ δ",
    searchable_by=["Mew \u2605 \u03b4", "Basic", "Star", "Mew"],
    subtypes=["Basic", "Star"],
    collector_number=101,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Mimicry",
            game_text="Choose an attack on 1 of your opponent's Pok\u00e9mon in play. Mimicry copies that attack. This attack does nothing if Mew Star doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Mew Star performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=mimicry_copy_any_opp_attack(),
        ),
        Attack(
            title="Rainbow Wave",
            game_text="Choose 1 basic Energy card attached to Mew Star. This attack does 20 damage to each of your opponent's Pok\u00e9mon that is the same type as the basic Energy card that you chose. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=rainbow_wave_per_type(20),
        ),
    ],
)