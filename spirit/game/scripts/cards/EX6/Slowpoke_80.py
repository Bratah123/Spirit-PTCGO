from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import confusion_wave

card = PokemonCardDef(
    guid="c9b79c83-efdf-51d1-a47c-6d700f553f34",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Confusion Wave",
            game_text="Both Slowpoke and the Defending Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=confusion_wave(),
        ),
    ],
)