from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    splintered_shards_gx,
    twilight_eyes,
)

card = PokemonCardDef(
    guid="df0ae499-28a3-51ed-8379-4122a38bd2d4",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=82,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=745,
    abilities=[
        Ability(
            title="Twilight Eyes",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=twilight_eyes,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Accelerock",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Splintered Shards-GX",
            game_text="This attack does 30 damage for each Energy card in your opponent's discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=splintered_shards_gx,
        ),
    ],
)