from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import swift


card = PokemonCardDef(
    guid="5b752be2-7eee-56d2-af9b-025179f5b44a",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=swift,
        ),
    ],
)
