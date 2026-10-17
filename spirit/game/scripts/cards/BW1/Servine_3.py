from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4d984b2-9ef2-5d30-a308-36f3dbee4cfd",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    display_name="Servine",
    searchable_by=["Servine", "Stage 1", "Servine"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Wrap",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)