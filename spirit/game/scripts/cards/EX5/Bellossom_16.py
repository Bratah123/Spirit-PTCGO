"""STUB: effect not implemented — do not guess mechanics.
Bellossom (EX5 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import heal_dance, miracle_powder, poke_power_condition

card = PokemonCardDef(
    guid="6a9af45a-314c-540a-8378-4070bb7e44c5",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2", "Bellossom"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Heal Dance",
            game_text="Once during your turn (before your attack), you may remove 2 damage counters from 1 of your Pok\u00e9mon. You can't use more than 1 Heal Dance Pok\u00e9-Power each turn. This power can't be used if Bellossom is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=heal_dance(),
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose 1 Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=miracle_powder(),
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)