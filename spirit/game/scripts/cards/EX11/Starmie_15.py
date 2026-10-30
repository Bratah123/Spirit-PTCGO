"""STUB: effect not implemented — do not guess mechanics.
Starmie δ (EX11 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import draw_cards_n, metal_navigation_attach, poke_power_condition
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="d194dc83-9df0-526f-9dbd-1034ab8c2eb4",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie δ",
    searchable_by=["Starmie \u03b4", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Metal Navigation",
            game_text="Once during your turn (before your attack), you may search your deck for a Metal Energy card and attach it to Starmie. Shuffle your deck afterward. This power can't be used if Starmie is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=metal_navigation_attach(),
        ),
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Energy Loop",
            game_text="Return an Energy card attached to Starmie to your hand.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=draw_cards_n(3),
        ),
    ],
)