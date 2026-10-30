"""STUB: effect not implemented — do not guess mechanics.
Blissey ex (EX10 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Triggers, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import blissful_support_on_evolve, energy_absorption

card = PokemonCardDef(
    guid="6bad01fd-2b72-5826-a1ac-1f3caf05f8b0",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blisseyex.Name",
    display_name="Blissey ex",
    searchable_by=["Blissey ex", "Stage 1", "ex", "Blisseyex"],
    subtypes=["Stage 1", "ex"],
    collector_number=101,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chanseyex.Name",
    family_id=242,
    abilities=[
        Ability(
            title="Blissful Support",
            game_text="Once during your turn, when you play Blissey ex from your hand to evolve 1 of your Pok\u00e9mon, you may discard all Energy cards attached to any number of your Pok\u00e9mon and remove all damage counters from those Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            # STUB: ability effect not implemented
            effect=blissful_support_on_evolve(),
        ),
        Attack(
            title="Energy Absorption",
            game_text="Attach up to 3 Energy cards from your discard pile to Blissey ex.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=energy_absorption(3),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
        ),
    ],
)