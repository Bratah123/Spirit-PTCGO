from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import sketch


card = PokemonCardDef(
    guid="34859ad0-bcb3-5f27-9ab9-a3508ea34fa6",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=235,
    abilities=[
        Attack(
            title="Sketch",
            game_text="If the Defending Pok\u00e9mon attacked last turn, and Smeargle was in play during that attack, Smeargle copies that attack except for its Energy costs and anything else required in order to use that attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=sketch,
        ),
    ],
)
