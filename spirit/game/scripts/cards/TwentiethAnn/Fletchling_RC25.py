from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.content.definitions import def_for


card = PokemonCardDef(
    guid="c49eb161-61c7-5d7c-85ab-eb6f552cb1b3",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic", "Fletchling"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=661,
    abilities=[
        Attack(
            title="Warble",
            game_text="Search your deck for up to 2 Fletchling, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(lambda c: getattr(def_for(c.archetype_id), "display_name", "") == "Fletchling", count=2, minimum=0, reveal=True, prompt="Choose up to 2 Fletchling"),
        ),
    ],
)