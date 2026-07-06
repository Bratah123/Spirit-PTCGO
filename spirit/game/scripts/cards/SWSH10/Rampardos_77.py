from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="56d87599-be1a-598a-943b-2c454f96db44",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
        ),
        Attack(
            title="Jurassic Hammer",
            game_text="If your opponent has 3 or fewer cards in their hand, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=240,
            effect=unimplemented,
        ),
    ],
)