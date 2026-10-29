from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    distortion_door,
    distortion_door_condition,
    shadow_impact,
)

card = PokemonCardDef(
    guid="5b0d70fa-83d3-59c6-88af-195d50ea7903",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title="Distortion Door",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, put 1 damage counter on 2 of your opponent's Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=distortion_door,
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            condition=distortion_door_condition,
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 4 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=shadow_impact
        ),
    ],
)