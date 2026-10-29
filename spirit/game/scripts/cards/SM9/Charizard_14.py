from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    continuous_blaze_ball,
    roaring_resolve,
)

card = PokemonCardDef(
    guid="013f5199-b5ad-5797-8b66-29ffeb56b6bc",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on this Pok\u00e9mon. If you do, search your deck for up to 2 Fire Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=roaring_resolve,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Continuous Blaze Ball",
            game_text="Discard all Fire Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=continuous_blaze_ball,
        ),
    ],
)