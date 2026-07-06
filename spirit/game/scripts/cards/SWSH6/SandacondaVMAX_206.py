from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0cf280a7-5cfa-53e0-8d56-942d7bcdef40",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaVMAX.Name",
    display_name="Sandaconda VMAX",
    searchable_by=["Sandaconda VMAX", "VMAX", "SandacondaVMAX"],
    subtypes=["VMAX"],
    collector_number=206,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaV.Name",
    family_id=844,
    abilities=[
        Attack(
            title="Sand Pulse",
            game_text="This attack also does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Cyclone",
            game_text="Move any amount of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)