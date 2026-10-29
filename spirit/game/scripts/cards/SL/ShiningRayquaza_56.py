"""STUB: effect not implemented — do not guess mechanics.
Shining Rayquaza (SL #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack, self_energy_discard_attack


card = PokemonCardDef(
    guid="fcf07ba2-2279-55cc-9eb1-7621f3edb783",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningRayquaza.Name",
    display_name="Shining Rayquaza",
    searchable_by=["Shining Rayquaza", "Basic", "ShiningRayquaza"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SL",
    rarity=Rarities.Shining,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=mill_attack(2, opponent=False),
        ),
        Attack(
            title="Sky Judgment",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)