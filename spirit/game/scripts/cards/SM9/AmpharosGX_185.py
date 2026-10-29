from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    electrical_gx,
    impact_bolt,
    power_recharge,
)

card = PokemonCardDef(
    guid="bff5c296-b150-57b3-81b3-317c51860de1",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosGX.Name",
    display_name="Ampharos-GX",
    searchable_by=["Ampharos-GX", "Stage 2", "GX", "AmpharosGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=185,
    set_code="SM9",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Power Recharge",
            game_text="Put all Electropower cards from your discard pile into your hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=power_recharge,
        ),
        Attack(
            title="Impact Bolt",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=150,
            effect=impact_bolt,
        ),
        Attack(
            title="Electrical-GX",
            game_text="Search your deck for up to 7 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=electrical_gx,
        ),
    ],
)