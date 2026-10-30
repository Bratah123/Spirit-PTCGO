from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="349d6bb8-d468-57c2-b79f-370d7aeab06c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)