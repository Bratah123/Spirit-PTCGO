from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="040da654-743a-5a6b-8b6a-02bbc45230d7",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    display_name="Shieldon",
    searchable_by=["Shieldon", "Stage 1", "Shieldon"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=410,
    abilities=[
        Attack(
            title="Hard Headbutt",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Confront",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)