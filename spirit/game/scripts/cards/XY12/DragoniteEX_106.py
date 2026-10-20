"""STUB: effect not implemented — do not guess mechanics.
Dragonite-EX (XY12 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="2e633160-bb23-5d8d-a04f-c071c0b762d6",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=106,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=149,
    abilities=[
        Ability(
            title="Pull Up",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may put 2 Basic Pok\u00e9mon (except for Dragonite-EX) from your discard pile into your hand.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(),
        ),
    ],
)