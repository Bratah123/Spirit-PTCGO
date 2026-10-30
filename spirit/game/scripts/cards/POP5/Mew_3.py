from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import copy_defending_attack, extra_draw_attach_if_ex


card = PokemonCardDef(
    guid="be3e8e6c-449a-52b6-a42b-d93ceb684037",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew δ",
    searchable_by=["Mew \u03b4", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pokémon's attacks. Copy copies that attack. This attack does nothing if Mew doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Mew performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_defending_attack(),
        ),
        Attack(
            title="Extra Draw",
            game_text="If your opponent has any Pokémon-ex in play, search your deck for up to 2 basic Energy cards and attach them to Mew. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=extra_draw_attach_if_ex(2),
        ),
    ],
)
