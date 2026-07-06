from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63affa94-46ab-5f4e-bcb6-bd412200d353",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1", "Sandaconda"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Coil",
            game_text="During your next turn, this Pok\u00e9mon's attacks do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)