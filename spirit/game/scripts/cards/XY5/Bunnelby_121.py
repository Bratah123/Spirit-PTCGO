"""STUB: effect not implemented — do not guess mechanics.
Bunnelby (XY5 #121): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import mill_attack


card = PokemonCardDef(
    guid="3c22761e-f127-577f-a8b1-553445779489",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    display_name="Bunnelby",
    searchable_by=["Bunnelby", "Basic", "Bunnelby"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=659,
    abilities=[
        ancient_trait('Ω Barrage'),
        Attack(
            title="Burrow",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=mill_attack(1),
        ),
        Attack(
            title="Rototiller",
            game_text="Shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)