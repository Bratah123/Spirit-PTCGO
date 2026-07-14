from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="5a7d0956-85c9-5fa2-9a98-aa110f18eba8",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Mirage Step",
            game_text="Search your deck for up to 3 Kirlia and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_bench(
                predicate=lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Kirlia",
                count=3,
                prompt="Choose up to 3 Kirlia to put onto your Bench.",
            ),
        ),
    ],
)