from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="916d33b5-f534-5982-b05e-1e5087a7e0e7",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarVMAX.Name",
    display_name="Malamar VMAX",
    searchable_by=["Malamar VMAX", "VMAX", "MalamarVMAX"],
    subtypes=["VMAX"],
    collector_number=122,
    set_code="SWSH2",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarV.Name",
    family_id=687,
    abilities=[
        Attack(
            title="Max Jammer",
            game_text="Your opponent reveals their hand. Choose a card you find there and put it on the bottom of their deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)