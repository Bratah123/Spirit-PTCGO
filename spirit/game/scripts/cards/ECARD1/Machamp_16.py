from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    terraforming, terraforming_condition, iron_fist,
)


card = PokemonCardDef(
    guid="32a165eb-6441-5fc1-9f15-1920ee6654c0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Terraforming",
            game_text="Once during your turn (before your attack), you may look at the top 4 cards of your deck and rearrange them as you like. This power can't be used if Machamp is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=terraforming_condition,
            effect=terraforming,
        ),
        Attack(
            title="Iron Fist",
            game_text="Count the number of Pok\u00e9mon you have in play with damage counters on them. Flip a coin. If heads, this attack does 50 damage plus 10 more damage for each of those Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=iron_fist,
        ),
    ],
)
