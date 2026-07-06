from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42a3f01c-012f-5d6f-8781-5d132f748fa0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonVMAX.Name",
    display_name="Umbreon VMAX",
    searchable_by=["Umbreon VMAX", "VMAX", "Single Strike", "UmbreonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=215,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    family_id=197,
    abilities=[
        Ability(
            title="Dark Signal",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Darkness",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)