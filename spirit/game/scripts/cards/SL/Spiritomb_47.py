"""STUB: effect not implemented — do not guess mechanics.
Spiritomb (SL #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.sl import cursed_whirlpool_passive


card = PokemonCardDef(
    guid="e07d3a7b-fdd9-5cac-9f30-8b749486398c",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=442,
    abilities=[
        Ability(
            title="Cursed Whirlpool",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon can't retreat.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=cursed_whirlpool_passive,
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=place_counters(3, 'choose_any_opponent'),
        ),
    ],
)