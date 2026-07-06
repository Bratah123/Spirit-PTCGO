from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dd46d0f3-cbe1-5248-99ac-4f5e4fbf8584",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitanVMAX.Name",
    display_name="Galarian Darmanitan VMAX",
    searchable_by=["Galarian Darmanitan VMAX", "VMAX", "GalarianDarmanitanVMAX"],
    subtypes=["VMAX"],
    collector_number=187,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitanV.Name",
    family_id=555,
    abilities=[
        Attack(
            title="Max Whiteout",
            game_text="This attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=200,
            effect=unimplemented,
        ),
    ],
)