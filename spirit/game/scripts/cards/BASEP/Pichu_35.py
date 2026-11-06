from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import is_baby_card
from spirit.game.card_effects.support_common import requires_bench_space, search_to_bench


card = PokemonCardDef(
    guid="637e27da-7edd-503d-8def-448aeae88927",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Baby", "Pichu"],
    subtypes=["Baby"],
    collector_number=35,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=172,
    abilities=[
        Attack(
            title="Let's Play!",
            game_text="Search your deck for a Baby Pok\u00e9mon card and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            condition=requires_bench_space(),
            effect=search_to_bench(
                predicate=is_baby_card,
                prompt="Choose a Baby Pokémon to put onto your Bench.",
            ),
        ),
    ],
)
