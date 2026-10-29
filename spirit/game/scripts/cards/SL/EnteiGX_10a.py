"""STUB: effect not implemented — do not guess mechanics.
Entei-GX (SL #10a): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, snipe_attack


card = PokemonCardDef(
    guid="89688863-b56c-57f8-90bb-d3ba1c732697",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnteiGX.Name",
    display_name="Entei-GX",
    searchable_by=["Entei-GX", "Basic", "GX", "EnteiGX"],
    subtypes=["Basic", "GX"],
    collector_number=79,
    set_code="SL",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Brave Burn-GX",
            game_text="This attack does 150 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(150),
        ),
    ],
)