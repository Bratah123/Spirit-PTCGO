"""STUB: effect not implemented — do not guess mechanics.
Haxorus (XY8 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack


card = PokemonCardDef(
    guid="9bcd06ba-9d3a-5c2a-9cfa-2afad9e850d9",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=111,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Dragon Dance",
            game_text="As long as this Haxorus is your Active Pok\u00e9mon, each of its attacks does 100 more damage (before applying Weakness and Resistance). You can't add more than 100 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=mill_attack(3, opponent=False),
        ),
    ],
)