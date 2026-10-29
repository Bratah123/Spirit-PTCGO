from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    mountain_pass,
    mountain_pass_condition,
)

card = PokemonCardDef(
    guid="af0a3e02-7aae-5aae-a8c5-6866fe7b6acb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    display_name="Trumbeak",
    searchable_by=["Trumbeak", "Stage 1", "Trumbeak"],
    subtypes=["Stage 1"],
    collector_number=165,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    family_id=731,
    abilities=[
        Ability(
            title="Mountain Pass",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your hand, you may reveal it. If you do, look at the top card of your opponent's deck and put this Pok\u00e9mon in the Lost Zone. If that card is a Supporter card, you may put it in the Lost Zone. If your opponent has no cards in their deck, you can't use this Ability.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=mountain_pass,
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            condition=mountain_pass_condition,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)