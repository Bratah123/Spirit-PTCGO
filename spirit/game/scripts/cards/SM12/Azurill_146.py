from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import growing_up

card = PokemonCardDef(
    guid="5586b2a5-e8ac-502b-b193-b28a28e055be",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=298,
    abilities=[
        Ability(
            title="Growing Up",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, attach a basic Energy card from your discard pile to your Active Pok\u00e9mon. If you use this Ability, your turn ends.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=growing_up,
        ),
    ],
)