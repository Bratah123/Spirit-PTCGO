from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import metronome_defending

card = PokemonCardDef(
    guid="5ccd36a0-b56a-5a95-99cf-951855f228ac",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefableex.Name",
    display_name="Clefable ex",
    searchable_by=["Clefable ex", "Stage 2", "ex", "Clefableex"],
    subtypes=["Stage 2", "ex"],
    collector_number=106,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Metronome",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Metronome copies that attack except for its Energy cost. (You must still do anything else in order to use that attack.) (No matter what type that Pok\u00e9mon is, Clefable ex's type is still Colorless.) Clefable ex performs that attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=metronome_defending,
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)