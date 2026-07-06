from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d1b5ff2-dfd8-5a8d-beff-e59a149c4d53",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonVMAX.Name",
    display_name="Duraludon VMAX",
    searchable_by=["Duraludon VMAX", "VMAX", "Single Strike", "DuraludonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=220,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonV.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Skyscraper",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have Special Energy attached.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Pulverization",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)