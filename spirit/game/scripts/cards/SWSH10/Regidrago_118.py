from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import dragons_hoard, dragons_hoard_condition

card = PokemonCardDef(
    guid="f11e9b72-9dd3-5dd7-b9de-cedeb13a60a5",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regidrago.Name",
    display_name="Regidrago",
    searchable_by=["Regidrago", "Basic", "Regidrago"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=895,
    abilities=[
        Ability(
            title="Dragon's Hoard",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw cards until you have 4 cards in your hand. You can't use more than 1 Dragon's Hoard Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=dragons_hoard_condition,
            shared_once_per_turn="Dragon's Hoard",
            effect=dragons_hoard,
        ),
        Attack(
            title="Giant Fangs",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
