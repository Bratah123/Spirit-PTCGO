"""Pichu (POP9 #11)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition, flip_search_pokemon


card = PokemonCardDef(
    guid="39ef82b8-2a87-5f91-a47a-39315b06c493",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Pikachu'),
            effect=baby_evolution('Pikachu')
        ),
        Attack(
            title="Find a Friend",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=flip_search_pokemon()
        ),
    ]
)