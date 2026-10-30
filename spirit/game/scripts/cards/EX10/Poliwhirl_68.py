"""STUB: effect not implemented — do not guess mechanics.
Poliwhirl (EX10 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import energy_ball_capped

card = PokemonCardDef(
    guid="238df109-3f94-5fc0-b9ee-0dbf1af34426",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    display_name="Poliwhirl",
    searchable_by=["Poliwhirl", "Stage 1", "Poliwhirl"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Energy Ball",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to Poliwhirl but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=energy_ball_capped(30, 10, 20),
        ),
    ],
)