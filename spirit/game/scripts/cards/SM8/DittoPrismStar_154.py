from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    almighty_evolution,
    almighty_evolution_condition,
)

card = PokemonCardDef(
    guid="600ddbd8-4185-502c-a662-cfdae26dc68f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoPrismStar.Name",
    display_name="Ditto {*}",
    searchable_by=["Ditto {*}", "Basic", "Prism Star", "DittoPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=154,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Almighty Evolution",
            game_text="Once during your turn (before your attack), you may put any Stage 1 card from your hand onto this Pok\u00e9mon to evolve it. You can't use this Ability during your first turn or the turn this Pok\u00e9mon was put into play.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=almighty_evolution,
            activation=Activations.ONCE_PER_TURN,
            condition=almighty_evolution_condition,
        ),
    ],
)