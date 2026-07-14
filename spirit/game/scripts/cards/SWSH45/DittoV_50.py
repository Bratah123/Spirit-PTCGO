from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import v_transformation, v_transformation_condition
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed8ed163-04e6-527e-a80a-bd0dd51bdffc",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    display_name="Ditto V",
    searchable_by=["Ditto V", "Basic", "V", "DittoV"],
    subtypes=["Basic", "V"],
    collector_number=50,
    set_code="SWSH45",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="V Transformation",
            game_text="Once during your turn, you may choose a Basic Pok\u00e9mon V from your discard pile and switch it with this Pok\u00e9mon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=v_transformation_condition,
            effect=v_transformation,
        ),
        Attack(
            title="Stick On",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                is_basic_energy_card, count=1, target="self",
                prompt="Choose a basic Energy card to attach to this Pokémon",
            ),
        ),
    ],
)