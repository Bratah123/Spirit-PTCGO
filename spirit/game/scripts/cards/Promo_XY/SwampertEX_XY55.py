"""STUB: effect not implemented — do not guess mechanics.
Swampert-EX (Promo_XY #XY55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="3ce942e2-615f-5678-9b3a-4ff7234c50e8",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SwampertEX.Name",
    display_name="Swampert-EX",
    searchable_by=["Swampert-EX", "Basic", "EX", "SwampertEX"],
    subtypes=["Basic", "EX"],
    collector_number=55,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=260,
    abilities=[
        Attack(
            title="Mud Flood",
            game_text="Reveal the top 4 cards of your deck. This attack does 40 more damage for each Water Energy you find there. Shuffle the revealed cards back into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Tackle",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=recoil_attack(20),
        ),
    ],
)