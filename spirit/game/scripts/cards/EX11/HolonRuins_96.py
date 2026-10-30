from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import holon_ruins_condition, holon_ruins_draw

card = StadiumCardDef(
    guid="b6efba11-3e78-5137-97ef-4f0b39e28a3c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonRuins.Name",
    display_name="Holon Ruins",
    searchable_by=["Holon Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Holon Ruins",
        game_text="Each player that has any Pokémon in play that has δ on its card may draw a card once during his or her turn. If the player does, he or she discards a card from his or her hand.",
        ability_type=AbilityTypes.POKE_POWER,
        activation=Activations.ONCE_PER_TURN,
        condition=holon_ruins_condition(),
        effect=holon_ruins_draw(),
    ),
)
