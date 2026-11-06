from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import undersea_ruins, undersea_ruins_condition


card = StadiumCardDef(
    guid="940dd877-bbd8-5fd1-ab4d-9590a4579952",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnderseaRuins.Name",
    display_name="Undersea Ruins",
    searchable_by=["Undersea Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Undersea Ruins",
        game_text="Once during each player's turn (before attacking), that player may flip a coin. If heads, that player chooses 1 of his or her Evolved Pokémon in play and discards the top Evolution card from that Pokémon, devolving it.",
        activation=Activations.ONCE_PER_TURN,
        condition=undersea_ruins_condition,
        effect=undersea_ruins,
    ),
)
