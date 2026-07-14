from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import look_at_top, search_attach_energy
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="920411e1-3b6e-5bc9-89db-966fe258f489",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Dreamy Revelation",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card back on top of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=look_at_top(2, take=1, rest="back",
                                prompt="Choose 1 of the top 2 cards to put into your hand."),
        ),
        Attack(
            title="Amazing Star",
            game_text="Search your deck for up to 7 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, count=7),
        ),
    ],
)