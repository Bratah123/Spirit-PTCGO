from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2fda4efc-1a09-53e0-aad6-54f3cbbf795b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Fusion Strike", "Toxtricity"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=108,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Ability(
            title="Maximum Downer",
            game_text="If all your Pok\u00e9mon in play are Fusion Strike Pok\u00e9mon, your opponent's Pok\u00e9mon VMAX in play get -30 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)