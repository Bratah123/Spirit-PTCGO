"""STUB: effect not implemented — do not guess mechanics.
Pyroar (XY2 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="7c71795f-ec1a-5fc0-b434-43fcf89e13c9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Ability(
            title="Intimidating Mane",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Basic Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Fang",
            game_text="You may discard a Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=discard_for_bonus(source='self-energy', predicate=_is_fire_energy, max_count=1, flat=30, prompt='You may discard a Fire Energy for 30 more damage'),
        ),
    ],
)