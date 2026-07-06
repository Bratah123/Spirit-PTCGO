from spirit.game.card_effects.trainers import star_alchemy
from spirit.game.data_utils import Ability, Activations, PokemonToolCardDef, is_pokemon_v
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    granted_abilities=[
        Ability(
            "Star Alchemy",
            "During your turn, you may search your deck for a card and put "
            "it into your hand. Then, shuffle your deck. "
            "(You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            condition=lambda board, player_id, pokemon: is_pokemon_v(pokemon.archetype_id),
            effect=star_alchemy,
        ),
    ],
    guid="be06e8eb-eaca-5016-9ff0-f19336d681e3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestSealStone.Name",
    display_name="Forest Seal Stone",
    searchable_by=["Forest Seal Stone", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=156,
    set_code="SWSH12",
    rarity=Rarities.RareHolo
)
