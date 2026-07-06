from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee37cae5-f2b7-56af-832a-e3c637e6b0b0",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    display_name="Morgrem",
    searchable_by=["Morgrem", "Stage 1", "Single Strike", "Morgrem"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=177,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Crushing Blow",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)