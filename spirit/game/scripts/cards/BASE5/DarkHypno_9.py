from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import bench_manipulation


card = PokemonCardDef(
    guid="11da496c-348f-5ff4-a9b9-1165b2207044",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHypno.Name",
    display_name="Dark Hypno",
    searchable_by=["Dark Hypno", "Stage 1", "DarkHypno"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Bench Manipulation",
            game_text="Your opponent flips a number of coins equal to the number of Pok\u00e9mon on his or her Bench. This attack does 20 damage times the number of tails. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=bench_manipulation,
        ),
    ],
)
