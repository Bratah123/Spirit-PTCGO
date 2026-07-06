from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93b2cb2f-e92f-58c4-9f0d-0b49688e19db",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name",
    display_name="Torterra",
    searchable_by=["Torterra", "Stage 2", "Torterra"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Evopress",
            game_text="This attack does 50 damage for each of your Evolution Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)