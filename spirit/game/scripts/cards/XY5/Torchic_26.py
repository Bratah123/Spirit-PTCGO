"""STUB: effect not implemented — do not guess mechanics.
Torchic (XY5 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="f6341a32-dc75-5264-b359-b32e8954db83",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        ancient_trait('Ω Barrage'),
        Attack(
            title="Flare Bonus",
            game_text="Discard a Fire Energy card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)