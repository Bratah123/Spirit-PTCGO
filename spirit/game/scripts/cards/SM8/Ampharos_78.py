from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack

from spirit.game.card_effects.sm8 import (
    unseen_flash,
    unseen_flash_condition,
)

card = PokemonCardDef(
    guid="db5ca5ed-986a-5ddb-98b8-050acd8a2727",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=78,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Unseen Flash",
            game_text="Once during your turn (before your attack), you may put 2 Lightning Energy cards from your hand in the Lost Zone. If you do, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unseen_flash,
            activation=Activations.ONCE_PER_TURN,
            condition=unseen_flash_condition,
        ),
        Attack(
            title="Split Bomb",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=snipe_attack(50, pool='any', count=2),
        ),
    ],
)