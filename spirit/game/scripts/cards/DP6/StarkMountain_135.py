"""Stark Mountain (DP6 #135)."""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import stark_mountain_ability

card = StadiumCardDef(
    guid="5a1c2410-eb89-569e-9709-ba7f582a1d06",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarkMountain.Name",
    display_name="Stark Mountain",
    searchable_by=["Stark Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=135,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Stark Mountain",
        game_text="Once during each player's turn, that player may choose a Fire or Fighting Energy attached to 1 of his or her Pokémon and move that Energy to 1 of his or her Pokémon.",
        ability_type=AbilityTypes.POKE_BODY,
        activation=Activations.ONCE_PER_TURN,
        effect=stark_mountain_ability(),
    ),
)
