from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import grab


card = PokemonCardDef(
    guid="5c100329-53d7-537c-80e4-07adf3167b07",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=190,
    abilities=[
        Attack(
            title="Grab",
            game_text="Choose a Trainer card attached to 1 of your opponent's Pok\u00e9mon. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=grab,
        ),
        Attack(
            title="Tail Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
