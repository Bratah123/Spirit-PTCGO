from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.ex import flip_knock_out_defender


card = PokemonCardDef(
    guid="e70fd49f-0a8b-57a7-8ef8-a4e9f1982c0d",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    display_name="Dusclops",
    searchable_by=["Dusclops", "Stage 1", "Dusclops"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Attack(
            title="Judgement",
            game_text="Flip 2 coins. If both of them are heads, the Defending Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=flip_knock_out_defender(),
        ),
        Attack(
            title="Random Curse",
            game_text="Put a total of 5 damage counters on all Defending Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=place_counters(5),
        ),
    ],
)
