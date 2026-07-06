from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5db3f2a-bd2a-5f4c-bd92-e5639bb833a5",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalVMAX.Name",
    display_name="Melmetal VMAX",
    searchable_by=["Melmetal VMAX", "VMAX", "MelmetalVMAX"],
    subtypes=["VMAX"],
    collector_number=48,
    set_code="PGO",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalV.Name",
    family_id=809,
    abilities=[
        Attack(
            title="G-Max Juggernaut",
            game_text="This attack does 60 more damage for each extra Metal Energy attached to this Pok\u00e9mon (in addition to this attack's cost). You can't add more than 120 damage in this way.",
            cost={PokemonTypes.METAL: 3},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)