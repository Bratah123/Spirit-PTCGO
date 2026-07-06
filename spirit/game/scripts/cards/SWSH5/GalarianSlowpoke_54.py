from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="843f8913-976d-512d-8b32-46b3eafe9068",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    display_name="Galarian Slowpoke",
    searchable_by=["Galarian Slowpoke", "Basic", "GalarianSlowpoke"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="Tantailizing",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)