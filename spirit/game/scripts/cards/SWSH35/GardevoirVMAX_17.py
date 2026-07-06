from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6fabb536-2341-533a-a50e-4f6b152fb674",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirVMAX.Name",
    display_name="Gardevoir VMAX",
    searchable_by=["Gardevoir VMAX", "VMAX", "GardevoirVMAX"],
    subtypes=["VMAX"],
    collector_number=17,
    set_code="SWSH35",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirV.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Max Cure",
            game_text="Heal 50 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)