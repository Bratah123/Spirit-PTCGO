from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11f1fd5d-9176-50c6-8bb1-2248342740a6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantVMAX.Name",
    display_name="Trevenant VMAX",
    searchable_by=["Trevenant VMAX", "VMAX", "TrevenantVMAX"],
    subtypes=["VMAX"],
    collector_number=14,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantV.Name",
    family_id=709,
    abilities=[
        Attack(
            title="Missing in the Forest",
            game_text="This attack does 40 damage for each Supporter card in your opponent's discard pile.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Max Tree",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)