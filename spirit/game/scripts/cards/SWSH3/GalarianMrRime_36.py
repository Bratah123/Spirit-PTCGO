from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f6bc1751-21f2-5e0e-bf61-04c023ebab4d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRime.Name",
    display_name="Galarian Mr. Rime",
    searchable_by=["Galarian Mr. Rime", "Stage 1", "GalarianMrRime"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    family_id=122,
    abilities=[
        Ability(
            title="Shuffle Dance",
            game_text="Once during your turn, you may switch 1 of your opponent's face-down Prize cards with the top card of their deck. (The cards stay face down.)",
            effect=unimplemented,
        ),
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)