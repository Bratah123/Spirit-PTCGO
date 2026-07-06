from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2962aa46-1df3-55e3-91be-1b88f5f31e72",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic", "Phantump"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=708,
    abilities=[
        Attack(
            title="Dark Guidance",
            game_text="Put a Basic Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)