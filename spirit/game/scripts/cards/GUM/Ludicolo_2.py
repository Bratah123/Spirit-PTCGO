from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.gum import table_service, table_service_condition

card = PokemonCardDef(
    guid="5b17e3eb-a1b6-502a-bf2a-50ae9d25c427",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="GUM",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=272,
    abilities=[
        Ability(
            title="Table Service",
            game_text="Once during your turn (before your attack), you may heal 30 damage from 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=table_service_condition,
            effect=table_service,
        ),
        Attack(
            title="Punch and Run",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=switch_self_attack(),
        ),
    ],
)
