from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import night_eyes, perish_song


card = PokemonCardDef(
    guid="4dcf9cd2-21e5-54c0-b403-5eb967410a4d",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic", "Misdreavus"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=200,
    abilities=[
        Attack(
            title="Night Eyes",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=night_eyes,
        ),
        Attack(
            title="Perish Song",
            game_text="If the Defending Pok\u00e9mon is Asleep and was attacked with Night Eyes during your last turn, it is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=perish_song,
        ),
    ],
)
