from spirit.game.card_effects.pokemon import pumpkin_pit
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04560a42-d19b-5255-9214-ab55f98a18ee",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic", "Pumpkaboo"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=710,
    abilities=[
        Ability(
            title="Pumpkin Pit",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Stadium in play.",
            trigger=Triggers.ON_PLAY,
            effect=pumpkin_pit,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
