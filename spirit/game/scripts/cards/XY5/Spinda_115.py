"""STUB: effect not implemented — do not guess mechanics.
Spinda (XY5 #115): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


card = PokemonCardDef(
    guid="fe928317-cb39-5348-9747-9be0ecb97809",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="Staggering Steps",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused. If tails, this Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Uproar",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(10),
        ),
    ],
)