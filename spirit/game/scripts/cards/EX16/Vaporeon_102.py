"""STUB: effect not implemented — do not guess mechanics.
Vaporeon ★ (EX16 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.card_effects.ex import blue_ray_on_bench
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="5c877e19-ad3f-5686-b135-bc94980816bb",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon ★",
    searchable_by=["Vaporeon \u2605", "Basic", "Star", "Vaporeon"],
    subtypes=["Basic", "Star"],
    collector_number=102,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=134,
    abilities=[
        Ability(
            title="Blue Ray",
            game_text="Once during your turn, when you put Vaporeon Star from your hand onto your Bench, you may remove all Special Conditions and 3 damage counters from each Active Pok\u00e9mon (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=blue_ray_on_bench(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
    ],
)