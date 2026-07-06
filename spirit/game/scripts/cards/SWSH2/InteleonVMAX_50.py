from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7faaa98-038f-5499-b403-9014ad9db931",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonVMAX.Name",
    display_name="Inteleon VMAX",
    searchable_by=["Inteleon VMAX", "VMAX", "InteleonVMAX"],
    subtypes=["VMAX"],
    collector_number=50,
    set_code="SWSH2",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    family_id=818,
    abilities=[
        Attack(
            title="Hydro Snipe",
            game_text="You may put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Max Bullet",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)