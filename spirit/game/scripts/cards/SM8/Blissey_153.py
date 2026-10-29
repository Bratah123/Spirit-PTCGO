from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, flip_damage

from spirit.game.card_effects.sm8 import (
    happiness_supplement,
    happiness_supplement_condition,
)

card = PokemonCardDef(
    guid="2d9ed1c1-16b7-5ff1-aee5-a8885ad02f0c",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=153,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happiness Supplement",
            game_text="Once during your turn (before your attack), you may remove a Special Condition from your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=happiness_supplement,
            activation=Activations.ONCE_PER_TURN,
            condition=happiness_supplement_condition,
        ),
        Attack(
            title="Powerful Slap",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy('self'), per_heads=80),
        ),
    ],
)