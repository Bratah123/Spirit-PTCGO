from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70e09fd7-213c-59e7-b987-11e408acfb2e",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Double Slash",
            game_text="Flip 2 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)