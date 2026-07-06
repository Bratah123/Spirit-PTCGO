from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f9dcb26-d56a-5603-8cdb-0c3a6902eece",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightVMAX.Name",
    display_name="Corviknight VMAX",
    searchable_by=["Corviknight VMAX", "VMAX", "CorviknightVMAX"],
    subtypes=["VMAX"],
    collector_number=110,
    set_code="SWSH5",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightV.Name",
    family_id=823,
    abilities=[
        Ability(
            title="Lustrous Body",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's Abilities done to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Hurricane",
            game_text="During your next turn, this Pok\u00e9mon can't use G-Max Hurricane.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)