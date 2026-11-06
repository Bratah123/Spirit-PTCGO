from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import has_typed_basic_energy, scorching_lava


card = PokemonCardDef(
    guid="d700ffb7-0af2-5166-a4b7-99aeb02a7f5e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Scorching Lava",
            game_text="Discard a Fire Energy card attached to Slugma in order to use this attack. The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            condition=has_typed_basic_energy(PokemonTypes.FIRE),
            effect=scorching_lava,
        ),
    ],
)
