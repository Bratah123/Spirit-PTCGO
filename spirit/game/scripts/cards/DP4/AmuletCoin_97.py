"""Amulet Coin (DP4 #97)."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import amulet_coin_eot_draw

card = PokemonToolCardDef(
    guid="b0151dd5-68b4-5509-8def-0c9415905bae",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletCoin.Name",
    display_name="Amulet Coin",
    searchable_by=["Amulet Coin", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Amulet Coin",
            game_text="If the Pokémon Amulet Coin is attached to is your Active Pokémon at the end of your turn, draw a card.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=amulet_coin_eot_draw(),
        ),
    ],
)
