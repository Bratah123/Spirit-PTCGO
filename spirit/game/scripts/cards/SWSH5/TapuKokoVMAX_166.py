from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f247e83c-c051-5d5a-9c73-2611af48bcad",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoVMAX.Name",
    display_name="Tapu Koko VMAX",
    searchable_by=["Tapu Koko VMAX", "VMAX", "TapuKokoVMAX"],
    subtypes=["VMAX"],
    collector_number=166,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoV.Name",
    family_id=785,
    abilities=[
        Attack(
            title="Max Shock",
            game_text="If you have more Prize cards remaining than your opponent, their Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)