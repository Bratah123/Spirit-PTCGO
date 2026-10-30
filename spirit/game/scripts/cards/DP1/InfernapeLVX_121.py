"""STUB: effect not implemented — do not guess mechanics.
Infernape LV.X (DP1 #121): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import look_at_top
from spirit.game.card_effects.dp import burning_head, flare_up, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="f90bda56-f793-59b1-b5ff-eb9af58af494",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeLVX.Name",
    display_name="Infernape LV.X",
    searchable_by=["Infernape LV.X", "Level-Up", "InfernapeLVX"],
    subtypes=["Level-Up"],
    collector_number=121,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    family_id=390,
    abilities=[
        Ability(
            title="Burning Head",
            game_text="Once during your turn (before your attack), you may look at the top 3 cards of your deck, choose 1 of them, and put it into your hand. Discard the other 2 cards. This power can't be used if Infernape is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(),
            activation=Activations.ONCE_PER_TURN,
            effect=burning_head(),
        ),
        Attack(
            title="Flare Up",
            game_text="Search your discard pile for 8 Fire Energy cards, show them to your opponent, and shuffle them into your deck. (This attack does nothing if you don't have 8 Fire Energy cards in your discard pile.)",
            cost={PokemonTypes.FIRE: 2},
            damage=150,
            effect=flare_up(8),
        ),
    ],
)