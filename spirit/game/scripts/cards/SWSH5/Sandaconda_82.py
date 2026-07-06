from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="298d1d7f-9206-5fd0-a53d-d09c1173194a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1", "Sandaconda"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Big Sand Cannon",
            game_text="Discard the top 6 cards of your deck. This attack does 60 damage for each Fighting Energy card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)