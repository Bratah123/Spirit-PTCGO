from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    attach_from_discard_then_counters, baby_evolution, baby_evolution_condition,
)


card = PokemonCardDef(
    guid="22b66d46-7e67-53e4-a242-8724fc0b7b85",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition("Pikachu"),
            effect=baby_evolution("Pikachu"),
        ),
        Attack(
            title="Energy Retrieval",
            game_text="Search your discard pile for up to 2 basic Energy cards and attach them to 1 of your Pok\u00e9mon. Put 1 damage counter on that Pok\u00e9mon for each Energy card attached in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard_then_counters(
                prompt="Choose up to 2 basic Energy cards to attach.",
            ),
        ),
    ],
)
