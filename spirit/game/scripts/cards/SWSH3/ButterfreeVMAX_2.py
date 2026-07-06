from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce6168a1-cd56-50c1-a99a-3d49564b2616",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ButterfreeVMAX.Name",
    display_name="Butterfree VMAX",
    searchable_by=["Butterfree VMAX", "VMAX", "ButterfreeVMAX"],
    subtypes=["VMAX"],
    collector_number=2,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ButterfreeV.Name",
    family_id=12,
    abilities=[
        Attack(
            title="G-Max Toxbreeze",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)