from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    haunt,
    vessel_of_life,
    vessel_of_life_condition,
)

card = PokemonCardDef(
    guid="10586aa5-0b4e-5290-8141-c389693024eb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Vessel of Life",
            game_text="Once during your turn (before your attack), you may discard all cards attached to this Pok\u00e9mon and attach it to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. When the Pok\u00e9mon this card is attached to is Knocked Out, your opponent takes 1 fewer Prize card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=vessel_of_life,
            activation=Activations.ONCE_PER_TURN,
            condition=vessel_of_life_condition,
        ),
        Attack(
            title="Haunt",
            game_text="Put 3 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=haunt
        ),
    ],
)