from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="07ae4cdd-fbf2-5da7-8616-adebdd551406",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceVMAX.Name",
    display_name="Cinderace VMAX",
    searchable_by=["Cinderace VMAX", "VMAX", "Single Strike", "CinderaceVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=45,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    family_id=815,
    abilities=[
        Attack(
            title="G-Max Fireball",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned. During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=unimplemented,
        ),
    ],
)