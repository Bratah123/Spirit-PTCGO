"""STUB: effect not implemented — do not guess mechanics.
Onix (EX10 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dig_deep_energy_to_hand

card = PokemonCardDef(
    guid="c9169519-5339-55a7-8aa6-cbb937eceec0",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=95,
    abilities=[
        Attack(
            title="Dig Deep",
            game_text="Search your discard pile for an Energy card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dig_deep_energy_to_hand(),
        ),
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)