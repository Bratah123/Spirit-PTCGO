from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="59d22193-66a4-5d7d-acde-cdf8cc4d1ac8",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Basic", "Elekid"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Electabuzz from your hand onto Elekid (this counts as evolving Elekid) and remove all damage counters from Elekid.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition("Electabuzz"),
            effect=baby_evolution("Electabuzz"),
        ),
        Attack(
            title="Gather Energy",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=search_attach_energy(
                predicate=is_basic_energy_card, count=1,
                prompt="Choose a basic Energy card to attach.",
            ),
        ),
    ],
)
