from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae03ce97-984b-53be-9073-c92cb23cb52b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Single Strike", "Lycanroc"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=87,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Rogue Fangs",
            game_text="This attack does 10 more damage for each Single Strike Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)