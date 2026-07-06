from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ecf0c178-7ba2-500d-bcaa-24627b4d12ca",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1", "Gourgeist"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Pandemonium",
            game_text="Reveal the top 6 cards of your deck. This attack does 60 damage for each Psychic Pok\u00e9mon you find there. Then, shuffle those Pok\u00e9mon back into your deck and discard the other cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)