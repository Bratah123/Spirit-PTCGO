from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import star_turn_switch, cross_wind_discard_all_energy

card = PokemonCardDef(
    guid="f0598f18-efd0-5830-9758-4f108b01dbcb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune ★",
    searchable_by=["Suicune \u2605", "Basic", "Star", "Suicune"],
    subtypes=["Basic", "Star"],
    collector_number=115,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Splashing Turn",
            game_text="Switch Suicune Star with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=star_turn_switch(20),
        ),
        Attack(
            title="Cross Wind",
            game_text="If you have less Prize cards left than your opponent, discard all Energy cards attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=70,
            effect=cross_wind_discard_all_energy(70),
        ),
    ],
)
