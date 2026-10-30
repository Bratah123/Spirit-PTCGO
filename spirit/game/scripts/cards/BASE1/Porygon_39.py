from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import conversion_1, conversion_2


card = PokemonCardDef(
    guid="e491b524-820d-5f6e-a906-0cc6fb6da769",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=137,
    abilities=[
        Attack(
            title="Conversion 1",
            game_text="If the Defending Pok\u00e9mon has a Weakness, you may change it to a type of your choice other than Colorless.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=conversion_1,
        ),
        Attack(
            title="Conversion 2",
            game_text="Change Porygon's Resistance to a type of your choice other than Colorless.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=conversion_2,
        ),
    ],
)
