from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import giant_growth


card = PokemonCardDef(
    guid="ae785192-4ed3-50af-9176-967039d0485e",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasDitto.Name",
    display_name="Koga's Ditto",
    searchable_by=["Koga's Ditto", "Basic", "KogasDitto"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=132,
    abilities=[
        Attack(
            title="Giant Growth",
            game_text="Flip a coin. If heads, Koga's Ditto's maximum HP is now 80 and Koga's Ditto's Pound attack's base damage is 30 instead of 10. (Benching Koga's Ditto ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=giant_growth,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
