"""STUB: effect not implemented — do not guess mechanics.
Metagross (EX5 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import metal_juncture, poke_power_condition, squared_attack

card = PokemonCardDef(
    guid="1bfec7e5-bff8-5c91-af13-9e5ae5e1563a",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Metal Juncture",
            game_text="As often as you like during your turn (before your attack), you may move a Metal Energy card attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon. This power can't be used if Metagross is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=metal_juncture(),
        ),
        Attack(
            title="Squared Attack",
            game_text="Flip 4 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=squared_attack(4, 30),
        ),
    ],
)