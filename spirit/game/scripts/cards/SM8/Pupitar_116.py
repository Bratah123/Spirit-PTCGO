from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    hard_shell_evolution,
)

card = PokemonCardDef(
    guid="1247e898-9587-5ab7-ad1c-fcecc4ee31cc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Hard Shell Evolution",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may prevent all damage done to this Pok\u00e9mon by your opponent's attacks until the end of your opponent's next turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=hard_shell_evolution,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)