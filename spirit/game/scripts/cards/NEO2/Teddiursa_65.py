from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import nap_time


card = PokemonCardDef(
    guid="f6e89ebc-4755-5494-9d93-bcb3cb8e8810",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=216,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Nap Time",
            game_text="Remove all damage counters from Teddiursa. Teddiursa is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=nap_time,
        ),
    ],
)
