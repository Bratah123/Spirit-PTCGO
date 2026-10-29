from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import crossing_cut_gx

from spirit.game.card_effects.sm10 import (
    cat_walk,
    cat_walk_condition,
    vengeance,
)

card = PokemonCardDef(
    guid="a688f499-5f84-5ff4-ac94-da699fd280b7",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PersianGX.Name",
    display_name="Persian-GX",
    searchable_by=["Persian-GX", "Stage 1", "GX", "PersianGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=227,
    set_code="SM10",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Cat Walk",
            game_text="Once during your turn (before your attack), if 1 of your Pok\u00e9mon-GX or Pok\u00e9mon-EX was Knocked Out during your opponent's last turn, you may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. You can't use more than 1 Cat Walk Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Cat Walk",
            condition=cat_walk_condition,
            effect=cat_walk
        ),
        Attack(
            title="Vengeance",
            game_text="This attack does 20 more damage for each Pok\u00e9mon in your discard pile. You can't add more than 180 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=vengeance
        ),
        Attack(
            title="Slash Back-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=crossing_cut_gx,
        ),
    ],
)