from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench, requires_bench_space
from spirit.game.card_effects.ecard import is_nidoran_basic


card = PokemonCardDef(
    guid="7d897483-330e-5884-b2e4-a589b91825b0",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran \u2640", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon card named Nidoran \u2640 or Nidoran \u2642 and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            condition=requires_bench_space(),
            effect=search_to_bench(
                is_nidoran_basic,
                prompt="Choose a Nidoran ♀ or Nidoran ♂ to put onto your Bench.",
            ),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
